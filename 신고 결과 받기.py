def solution(id_list, report, k):
    humandict = {}

    answer = [0 for _ in range(len(id_list))]
    reportedict = [0 for _ in range(len(id_list))]  # 사람별 신고당한 횟수 저장
    reportboard = [[0] * len(id_list) for _ in range(len(id_list))]  # 사람별 신고 여부 저장
    reporter = ""
    reported = ""
    for i in range(0, len(id_list)):
        humandict[id_list[i]] = i

    for i in range(0, len(report)):
        reporter, reported = report[i].split()

        if (reportboard[humandict[reporter]][humandict[reported]] == 0):
            reportedict[humandict[reported]] += 1
            reportboard[humandict[reporter]][humandict[reported]] = 1

    for i in range(0, len(id_list)):
        for j in range(0, len(id_list)):
            if ((reportboard[i][j] == 1) and (reportedict[j] >= k)):
                answer[i] += 1

    return answer