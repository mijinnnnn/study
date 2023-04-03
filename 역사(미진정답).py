
#
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    n, k = map(int, read().rstrip().split())
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(k):
        r,c = map(int, read().rstrip().split())
        graph[r][c] = -1
        graph[c][r] = 1

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1, n+1):
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1

    s = int(read().rstrip())
    # print(s)
    res = []
    for i in range(s):
        r, c = map(int, read().rstrip().split())
        res.append(graph[r][c])

    for i in res:
        print(i)

if __name__ == '__main__':
    main()