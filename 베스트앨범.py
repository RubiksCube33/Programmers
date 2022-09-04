import operator


def solution(genres, plays):
    song_dict = {}
    ranking_dict = {}
    answer = []

    for i in range(0, len(genres)):
        if (genres[i] in song_dict):
            song_dict[genres[i]] += plays[i]

            if (genres[i] + "1") in ranking_dict:
                if (ranking_dict[genres[i] + "A"] < plays[i]):
                    ranking_dict[genres[i] + "1"] = ranking_dict[genres[i] + "0"]
                    ranking_dict[genres[i] + "B"] = ranking_dict[genres[i] + "A"]
                    ranking_dict[genres[i] + "0"] = i
                    ranking_dict[genres[i] + "A"] = plays[i]
                elif (ranking_dict[genres[i] + "B"] < plays[i]):
                    ranking_dict[genres[i] + "1"] = i
                    ranking_dict[genres[i] + "B"] = plays[i]
            else:
                if (ranking_dict[genres[i] + "A"] < plays[i]):
                    ranking_dict[genres[i] + "1"] = ranking_dict[genres[i] + "0"]
                    ranking_dict[genres[i] + "B"] = ranking_dict[genres[i] + "A"]
                    ranking_dict[genres[i] + "0"] = i
                    ranking_dict[genres[i] + "A"] = plays[i]
                else:
                    ranking_dict[genres[i] + "1"] = i
                    ranking_dict[genres[i] + "B"] = plays[i]

        else:
            song_dict[genres[i]] = plays[i]
            ranking_dict[genres[i] + "0"] = i
            ranking_dict[genres[i] + "A"] = plays[i]

    song_dict_sorted = sorted(song_dict.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(0, len(song_dict_sorted)):
        answer.append(ranking_dict[song_dict_sorted[i][0] + "0"])
        if (song_dict_sorted[i][0] + "1") in ranking_dict:
            answer.append(ranking_dict[song_dict_sorted[i][0] + "1"])

    return answer