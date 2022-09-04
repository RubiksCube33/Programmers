def solution(numbers, hand):

    answer = ""
    position_left = 10
    position_right = 11 #초기값 위치 = 10,11(특수문자 위치 *,#을 10과 11에 대응)
    coordinate_left_x = 100
    coordinate_left_y = 100
    coordinate_right_x = 100
    coordinate_right_y = 100
    coordinate_num_x = 100
    coordinate_num_y = 100
    length_left = 100
    length_right = 100 #할당 안된 부분 전부 100으로 퉁침 (다익스트라 inf값으로 초기세팅하는것과 비슷하게 함)

    coordinate = {}
    coordinate[10] = [3,0]
    coordinate[0] = [3,1]
    coordinate[11] = [3,2] #맨 아랫줄은 특수문자로 처리, 수동으로 3개 좌표 할당

    for i in range(1, 10):
        coordinate[i] = [(i-1)//3,(i-1)%3] #나머지 x,y 좌표 자동으로 할당

    for i in range(0,len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += "L"
            position_left = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += "R"
            position_right = numbers[i]
        else:
            coordinate_num_x,coordinate_num_y = coordinate[numbers[i]]
            coordinate_left_x,coordinate_left_y = coordinate[position_left]
            coordinate_right_x,coordinate_right_y = coordinate[position_right]
            length_left = abs(coordinate_left_x-coordinate_num_x) + abs(coordinate_left_y-coordinate_num_y)
            length_right = abs(coordinate_right_x-coordinate_num_x) + abs(coordinate_right_y-coordinate_num_y)

            if(length_left < length_right):
                answer+="L"
                position_left = numbers[i]
            elif(length_right < length_left):
                answer+="R"
                position_right = numbers[i]
            else:
                if hand=="left":
                    answer+="L"
                    position_left = numbers[i]
                else:
                    answer+="R"
                    position_right = numbers[i]

    return answer