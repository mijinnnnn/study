from collections import deque
import time
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def print_(A):
    for i in range(len(A)):
        print(A[i])

def dfs(r,c):

    global visited, A, R, C, temp

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= R or nc <0 or nc >= C or visited[nr][nc] != 0:
            continue

        if A[nr][nc] == 1:
            visited[nr][nc] = 1
            temp.append((nr,nc))
            continue
        dfs(nr,nc)

def main():
    global visited, A, R, C, temp

    R,C = map(int, read().rstrip().split())

    A = []
    ch = 0
    for _ in range(R):
        temp = list(map(int, read().rstrip().split()))
        ch += temp.count(1)
        A.append(temp)

    # print_(A)
    time = 0
    while True:
        visited = [[0 for c in range(C)]for _ in range(R)]
        temp = []
        dfs(0,0)
        cnt = len(temp)
        for r,c in temp:
            A[r][c] = 0
        ch -= cnt
        time += 1
        if ch <= 0:
            print(time)
            print(cnt)
            break

if __name__ == '__main__':
    main()


