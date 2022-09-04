def solution(N, stages):
    answer = [0 for i in range(0, N)]
    clear = [0 for i in range(N + 2)]
    fail = [0 for i in range(N + 2)]
    tempanswer = [[0 for i in range(2)] for i in range(N)]

    for i in range(0, len(stages)):
        fail[stages[i]] += 1
        for j in range(1, stages[i] + 1):
            clear[j] += 1

    for i in range(0, N):
        if (clear[i + 1] != 0):
            tempanswer[i][0] = fail[i + 1] / clear[i + 1]
            tempanswer[i][1] = i + 1
        else:
            tempanswer[i][1] = i + 1

    tempanswer.sort(key=lambda x: (-x[0], x[1]))

    for i in range(0, N):
        answer[i] = tempanswer[i][1]

    return answer