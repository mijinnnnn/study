import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c,h):
    global A, N, visited
    visited[r][c] = 1
    for i in range(4):
        nr = r +dr[i]
        nc = c +dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] != 0:
            continue
        if A[nr][nc] <= h:
            continue
        dfs(nr,nc,h)

def main():
    global N, A, visited
    N = int(read())
    A = []
    max_A = 0


    for i in range(N):
        temp = list(map(int, read().rstrip().split()))
        max_A = max(max(temp),max_A)
        A.append(temp)
    cnt_max = -1

    for i in range(max_A):
        cnt = 0
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if A[r][c] > i and visited[r][c] == 0:
                    dfs(r,c,i)
                    cnt += 1
        # print(cnt)
        cnt_max = max(cnt, cnt_max)
    # print(max_A)
    print(cnt_max)


if __name__ == '__main__':
    main()