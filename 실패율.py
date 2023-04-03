
N = 10
stages = [2, 1, 2, 11, 2, 4, 3, 3]


# def solution(N, stages):
#     temp = []
#     players = len(stages)
#     test_range = min(N+1, max(stages)+1)
#     for i in range(1,test_range):
#         cur_p = stages.count(i)
#         f_rate = cur_p / players
#         temp.append((i, f_rate))
#         players -= cur_p
#
#     temp = sorted(temp, key=lambda x: (x[1], -x[0]), reverse=True)
#     answer = [x[0] for x in temp]
#     if len(answer) < N:
#         for i in range(test_range,N+1):
#             answer.append(i)
#
#     return answer

def solution(N, stages):
    temp = []
    players = len(stages)

    for i in range(1, N + 1):
        if players == 0:
            temp.append((i, 0))

        else:
            cur_p = stages.count(i)
            f_rate = cur_p / players
            temp.append((i, f_rate))
            players -= cur_p

    temp = sorted(temp, key=lambda x: (x[1], -x[0]), reverse=True)
    answer = [x[0] for x in temp]

    return answer


print(solution(N, stages))