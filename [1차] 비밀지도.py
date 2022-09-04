def solution(n, arr1, arr2):
    answer = []
    TempBinaryLine1 = ""
    TempBinaryLine2 = ""
    TempAnswer = ""
    TempNum = 0

    for i in range(0, n):
        TempAnswer = ""

        TempBinaryLine1 = bin(int(arr1[i]))
        TempBinaryLine2 = bin(int(arr2[i]))

        TempBinaryLine1 = TempBinaryLine1[2:]
        TempBinaryLine2 = TempBinaryLine2[2:]

        while len(TempBinaryLine1) < n:
            TempBinaryLine1 = "0" + TempBinaryLine1

        while len(TempBinaryLine2) < n:
            TempBinaryLine2 = "0" + TempBinaryLine2

        for j in range(0,n):
            TempNum = int(TempBinaryLine1[j]) + int(TempBinaryLine2[j])
            if TempNum:
                TempAnswer = TempAnswer + "#"
            else:
                TempAnswer = TempAnswer + " "
        answer.append(TempAnswer)

    return answer