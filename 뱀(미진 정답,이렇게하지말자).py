import sys
from collections import deque
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N = int(read().rstrip())  #보드크기
    K = int(read().rstrip()) #사과수
    a = [[0]*N for _ in range(N)]  #사과 위치 지도
    Q = deque()
    Q.append([0,0])   #뱀

    for i in range(K):
        r, c = map(int, read().rstrip().split())
        a[r-1][c-1] = 1

    L = int(read().rstrip())  #변환 횟수

    dic_dir = {}

    for _ in range(L):
        c, d = read().rstrip().split()
        dic_dir[int(c)] = str(d)

    cur_dir = 0
    cnt = 0

    while True:
        if cnt in dic_dir:
            if dic_dir[cnt] == "D":
                cur_dir = (cur_dir+1)%4
            elif dic_dir[cnt] == "L":
                cur_dir = (cur_dir-1)%4

        if cur_dir == 0:
            x,y = Q[0]
            y += 1
            if x < 0 or x >= N or y < 0 or y >= N:
                cnt += 1
                break
            if [x,y] in Q:
                cnt += 1
                break
            if a[x][y] == 1:
                a[x][y] = 0
                Q.appendleft([x,y])
            else:
                Q.appendleft([x, y])
                Q.pop()
            cnt += 1
        if cur_dir == 1:
            x,y = Q[0]
            x += 1
            if x < 0 or x >= N or y < 0 or y >= N:
                cnt += 1
                break
            if [x, y] in Q:
                cnt += 1
                break
            if a[x][y] == 1:
                a[x][y] = 0
                Q.appendleft([x,y])
            else:
                Q.appendleft([x, y])
                Q.pop()
            cnt += 1

        if cur_dir == 2:

            x,y = Q[0]
            y -=1
            if x < 0 or x >= N or y < 0 or y >= N:
                cnt += 1
                break
            if [x,y] in Q:
                cnt += 1
                break

            if a[x][y] == 1:
                a[x][y] = 0
                Q.appendleft([x,y])

            else:
                Q.appendleft([x,y])
                Q.pop()
            cnt += 1


        if cur_dir == 3:
            x,y = Q[0]
            x -= 1
            if x < 0 or x >= N or y < 0 or y >= N:
                cnt += 1
                break
            if [x,y] in Q:
                cnt += 1
                break
            if a[x][y] == 1:
                a[x][y] = 0
                Q.appendleft([x, y])

            else:
                Q.appendleft([x, y])
                Q.pop()
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()


# import sys
# from collections import deque
#
# read = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# def main():
#     N = int(read().rstrip())  # 보드 크기
#     K = int(read().rstrip()) # 사과 수
#     a = [[0]*N for _ in range(N)]  # 사과 위치 지도
#     Q = deque()
#     Q.append([0,0])   # 뱀
#
#     for i in range(K):
#         r, c = map(int, read().rstrip().split())
#         a[r-1][c-1] = 1 # 사과의 위치를 입력 받을 때 1을 입력해주었습니다.
#
#     L = int(read().rstrip())  # 변환 횟수
#
#     dic_dir = {}
#
#     for _ in range(L):
#         c, d = read().rstrip().split()
#         dic_dir[int(c)] = str(d)
#
#     cur_dir = 0
#     cnt = 0
#
#     while True:
#         # 뱀의 머리 위치
#         x, y = Q[0]
#
#         if cnt in dic_dir:
#             if dic_dir[cnt] == "D":
#                 cur_dir = (cur_dir+1)%4
#             elif dic_dir[cnt] == "L":
#                 cur_dir = (cur_dir-1)%4
#
#         # 다음 이동할 위치
#         if cur_dir == 0:
#             y += 1
#         elif cur_dir == 1:
#             x += 1
#         elif cur_dir == 2:
#             y -= 1
#         elif cur_dir == 3:
#             x -= 1
#
#         # 다음 이동할 위치가 보드를 벗어난 경우
#         if x < 0 or x >= N or y < 0 or y >= N:
#             cnt += 1
#             break
#
#         # 다음 이동할 위치가 뱀의 몸통인 경우
#         if [x, y] in Q:
#             cnt += 1
#             break
#
#         # 다음 이동할 위치에 사과가 있는 경우
#         if a[x][y] == 1:
#             a[x][y] = 0
#             Q.appendleft([x, y])
#         # 다음 이동할 위치에 사과가 없는 경우
#         else:
#             Q.appendleft([x, y])
#             Q.pop()
#
#         cnt += 1
#         print(Q)
#
#     print(cnt)
#
# if __name__ == '__main__':
#     main()