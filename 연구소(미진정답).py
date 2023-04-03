import sys
from itertools import combinations
import copy
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    global visited, B, R, C
    visited[r][c] = 1


    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= R or nc <0 or nc >=C or visited[nr][nc] != 0:
            continue
        if B[nr][nc] == 0:
            B[nr][nc] = 2
            dfs(nr,nc)

def main():
    global visited, B, R, C
    R,C = map(int, read().rstrip().split())
    A = []
    zero_list = []

    for r in range(R):
        temp = list(map(int,read().rstrip().split()))
        A.append(temp)

    for r in range(R):
        for c in range(C):
            if A[r][c] == 0:
                zero_list.append((r,c))
    res = 0

    # C = list(combinations(zero_list, 3))
    for add_wall in list(combinations(zero_list,3)):
        B = copy.deepcopy(A)
        visited = [[0 for _ in range(C)]for _ in range(R)]
        for r,c in add_wall:
            B[r][c] = 1
        # print(B)
        for r in range(R):
            for c in range(C):
                if B[r][c] == 2 and visited[r][c] == 0:
                    dfs(r,c)
        # print(B)
        cnt = 0
        for i in range(R):
            cnt += B[i].count(0)
        # print(cnt)
        res = max(res,cnt)
    #
    print(res)

    # print(C)


if __name__ == '__main__':
    main()