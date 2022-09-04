def solution(number, k):
    answer = ""
    index = temp = 0
    for i in range(0,len(number)-k):
        for j in range(index,k+len(answer)+1):
            if int(number[j]) > temp:
                temp = int(number[j])
                index = j+1
                if int(number[j] == 9):
                    break
        answer += str(temp)
        temp = 0
    return answer