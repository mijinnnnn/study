# 1 20:00

import sys
read = sys.stdin.readline

global res_1, res_2, point_1, point_2,win_1, win_2


def calc(m1,s1,m2,s2):
    global win_1, win_2
    min = m1 -m2
    sec = s1 -s2
    if sec > 59:
        sec -= 60
        min += 1
    elif sec < 0:
        sec += 60
        min -= 1

    return [min, sec]

def count_time(team, T_min, T_sec):
    global res_1, res_2, point_1, point_2, win_1, win_2

    if team == 1:
        point_1 += 1
        if point_1 - point_2 == 1: #지다가 이기기 시작
            win_1 = [T_min, T_sec]

        elif point_1 == point_2:  #동점이 됨. #원래 지고 있었단 뜻.
            if win_2 != [0,0]:
                temp = calc(T_min,T_sec,win_2[0],win_2[1])
                res_2 = calc(res_2[0], res_2[1], -temp[0], -temp[1])
            win_1 = [0, 0]
            win_2 = [0, 0]

    elif team == 2:
        point_2 += 1
        if point_2 - point_1 == 1: #지다가 이기기 시작
            win_2 = [T_min, T_sec]

        elif point_1 == point_2:  #동점이 됨. #원래 지고 있었단 뜻.
            if win_1 != [0,0]:
                temp = calc(T_min,T_sec,win_1[0],win_1[1])
                res_1 = calc(res_1[0], res_1[1], -temp[0], -temp[1])
            win_1 = [0,0]
            win_2 = [0,0]


def main():
    global res_1, res_2, point_1, point_2, win_1, win_2
    N = int(read())
    # get_point = []

    res_1 = [0,0]
    res_2 = [0,0]
    point_1 = 0
    point_2 = 0
    win_1 = [0,0]
    win_2 = [0,0]

    for i in range(N):

        team, T = map(str, read().rstrip().split())
        T_min, T_sec = map(int, T.split(":"))
        count_time(int(team), T_min, T_sec)
        # print(T_min, T_sec)
        # get_point.append([int(team), T_min, T_sec])
    if win_1 != [0,0]:
        res_1 = calc(48, 00, win_1[0],win_1[1])

    if win_2 !=[0,0]:
        res_2 = calc(48, 00, win_2[0],win_2[1])


    print(f'{int(res_1[0]):02d}:{int(res_1[1]):02d}')
    print(f'{int(res_2[0]):02d}:{int(res_2[1]):02d}')


if __name__ == '__main__':
    main()
    # zfill(7)