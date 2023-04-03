
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = 1e9

def main():
    V = int(read().rstrip())
    E = int(read().rstrip())
    graph = [[INF for _ in range(V+1)]for _ in range(V+1)]

    for i in range(V+1):
        graph[i][i] = 0

    for i in range(E):
        start, end, dist = map(int, read().rstrip().split())
        graph[start][end] = min(dist, graph[start][end])

    for k in range(1,V+1):
        for i in range(1,V+1):
            for j in range(1,V+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

    for i in range(1,V+1):
        for j in range(1,V+1):
            if graph[i][j] == INF:
                print(0,end = ' ')
            else:
                print(graph[i][j],end = ' ')
        print()



if __name__ == '__main__':
    main()


