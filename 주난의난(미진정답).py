
import sys
from collections import deque
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global A, visited, x2, y2, next_Q,R,C ,flag
    Q = deque()
    for i in next_Q:
        Q.append(i)

    next_Q = []
    x,y = Q[0][0], Q[0][1]
    visited[x][y] = 1

    while Q:
        r = Q[0][0]
        c = Q[0][1]
        Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr == x2 and nc == y2:
                flag = False
                return
            if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or A[nr][nc] == -2:
                continue
            if A[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append((nr,nc))
            elif A[nr][nc] == 1:
                visited[nr][nc] = 1
                next_Q.append((nr, nc))
    return

def main():
    global A, visited, x2,y2, next_Q,R,C ,flag
    R, C = map(int, read().rstrip().split())
    x1,y1, x2, y2 = map(int, read().rstrip().split())
    x1,y1, x2, y2  = x1-1,y1-1, x2-1, y2-1


    A = [[0 for c in range(C)]for r in range(R)]

    temp = []
    visited = [[0 for c in range(C)]for r in range(R)]
    for i in range(R):
        temp1 = list(read().rstrip())
        temp.append(temp1)

    for r in range(R):
        for c in range(C):
            if temp[r][c] == '0' or temp[r][c] == '1':
                A[r][c] = int(temp[r][c])
            else:
                A[r][c] = -2
    flag = True
    cnt = 0
    next_Q = [(x1,y1)]

    while flag:
        bfs()
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()


