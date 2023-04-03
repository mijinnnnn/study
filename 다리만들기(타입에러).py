
from collections import deque
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def mat_print(A):
    for i in range(len(A)):
        print(A[i])

def bfs(r,c,visited1):
    global  N, A, temp_list, cnt

    Q = deque()
    Q.append((r,c))
    visited1[r][c] =1

    while Q:
        r = Q[0][0]
        c = Q[0][1]
        Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited1[nr][nc] != 0:
                continue

            if A[nr][nc] == cnt:
                continue

            if A[nr][nc] != 0:
                return visited1[r][c] -1

            visited1[nr][nc] = visited1[r][c] + 1
            Q.append((nr, nc))

def dfs(r,c):
    global visited, N, A, temp_list,cnt

    visited[r][c] = 1
    A[r][c] = cnt

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] != 0:
            continue
        if A[nr][nc] == 0:
            temp_list.append((r,c))
            continue
        dfs(nr,nc)


def main():
    global visited, N, A, temp_list,cnt
    N = int(read().rstrip())
    A = []

    for i in range(N):
        temp = list(map(int, read().rstrip().split()))
        A.append(temp)

    # mat_print(A)
    visited = [[0 for _ in range(N)]for _ in range(N)]
    cnt = 2
    res = int(1e9)
    for r in range(N):
        for c in range(N):
            if A[r][c] == 1 and visited[r][c] == 0:
                temp_list = []
                dfs(r,c)
                temp_min = int(1e9)
                # print(temp_list)

                for r,c in temp_list:
                    # print(r,c)
                    visited1 = [[0 for _ in range(N)] for _ in range(N)]
                    temp_min = min(bfs(r,c,visited1),temp_min)
                    # print(visited1)

                res = min(temp_min, res)
                cnt += 1

    print(res)


    # mat_print(A)

if __name__ == '__main__':
    main()


