def solution(board, moves):
    answer = 0
    catch = 0
    poppedstack = [0]

    for i in range(0,len(moves)):
        if(board[len(board[moves[i]-1])-1][moves[i]-1] != 0):
            for j in range(0,len(board[moves[i]-1])):
                if(board[j][moves[i]-1]) != 0:
                    catch = board[j][moves[i]-1]
                    board[j][moves[i]-1] = 0
                    break
        else: catch = 0
        if(catch != 0):
            if(poppedstack[-1] == catch):
                poppedstack.pop()
                answer += 2
            else:
                poppedstack.append(catch)


    return answer