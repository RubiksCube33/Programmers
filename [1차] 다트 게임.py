def solution(dartResult):
    answer = 0
    points = [100]

    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit() == False:
            if(dartResult[i] == "S"):
                answer += points[-1]

            elif(dartResult[i] == "D"):
                answer += points[-1]**2
                points[-1] **= 2

            elif(dartResult[i] == "T"):
                answer += points[-1]**3
                points[-1] **= 3

            elif(dartResult[i] == "*"):
                answer += points[-1]
                points[-1] *= 2

                if len(points) >= 2 :
                    answer += points[-2]
                    points[-2] *= 2

            elif(dartResult[i] == "#"):
                answer -= points[-1] * 2
                points[-1] -= points[-1] * 2

        else:
            if dartResult[i] == "0":
                if i >= 1 :
                    if dartResult[i-1] == "1" :
                        if len(points) >= 1 : points[-1] = 10
                        else : points.append(10)
                    else:points.append(0)
            else:points.append(int(dartResult[i]))

    return answer