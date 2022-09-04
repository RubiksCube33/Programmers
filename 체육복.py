def solution(n, lost, reserve):
    answer = 0
    arr = [1 for i in range(n)]

    for i in range(0, len(lost)):
        arr[lost[i] - 1] -= 1

    for i in range(0, len(reserve)):
        arr[reserve[i] - 1] += 1

    for i in range(0, n - 1):
        if (arr[i] == 2) and (arr[i + 1] == 0):
            arr[i] -= 1
            arr[i + 1] += 1
        elif (arr[i] == 0) and (arr[i + 1] == 2):
            arr[i + 1] -= 1
            arr[i] += 1

    for i in range(0, n):
        if (arr[i] > 0):
            answer += 1

    return answer