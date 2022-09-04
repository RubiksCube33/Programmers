def solution(places):
    answer = []
    socialdist = True

    for i in range(0, 5):
        socialdist = True
        for j in range(0, 5):
            if socialdist == False: break
            for k in range(0, 5):
                if socialdist == False: break

                if places[i][j][k] == "P":

                    if (j + 1 < 5):
                        if places[i][j + 1][k] == "P":
                            socialdist = False
                            break
                        if places[i][j + 1][k] != "X":
                            if (j + 2 < 5):
                                if places[i][j + 2][k] == "P":
                                    socialdist = False
                                    break

                    if (k + 1 < 5):
                        if places[i][j][k + 1] == "P":
                            socialdist = False
                            break
                        if places[i][j][k + 1] != "X":
                            if (k + 2 < 5):
                                if places[i][j][k + 2] == "P":
                                    socialdist = False
                                    break

                    if (j + 1 < 5) and (k + 1 < 5):
                        if places[i][j + 1][k + 1] == "P":
                            if (places[i][j + 1][k] != "X") or (places[i][j][k + 1] != "X"):
                                socialdist = False
                                break
                    if (j + 1 < 5) and (k - 1 >= 0):
                        if places[i][j + 1][k - 1] == "P":
                            if (places[i][j + 1][k] != "X") or (places[i][j][k - 1] != "X"):
                                socialdist = False
                                break

        if socialdist:
            answer.append(1)
        else:
            answer.append(0)

    return answer