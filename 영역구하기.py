import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global R, C, A, visited, res
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or A[nr][nc] == 0:
            continue
        dfs(nr, nc)
        res += 1


def main():
    global R, C, A, visited, res

    R, C, K = map(int, read().rstrip().split())
    A = [[1 for c in range(C)] for r in range(R)]
    visited = [[0 for c in range(C)] for r in range(R)]

    for i in range(K):
        t = list(map(int, read().rstrip().split()))
        for r in range(t[1], t[3]):
            for c in range(t[0], t[2]):
                A[r][c] = 0

    res_li = []
    cnt = 0
    for r in range(R):
        for c in range(C):
            if A[r][c] == 1 and visited[r][c] == 0:
                res = 1
                dfs(r, c)
                cnt += 1
                res_li.append(res)

    res_li.sort()
    print(cnt)
    print(*res_li)


if __name__ == '__main__':
    main()