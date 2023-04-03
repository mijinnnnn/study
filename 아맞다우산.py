
import sys
from collections import deque
from itertools import permutations
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(r1,c1,r2,c2):
    global visited, A, C, R
    visited[r1][c1] = 1
    Q = deque()
    Q.append((r1,c1))

    while Q:
        r = Q[0][0]
        c = Q[0][1]
        Q.popleft()
        if r == r2 and c == c2:
            return visited[r][c]-1
        for i in range(4):
            nr = r +dr[i]
            nc = c +dc[i]
            if nr < 0 or nr >=R or nc < 0 or nc >= C or visited[nr][nc] != 0 or A[nr][nc] == "#":
                continue
            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr,nc))


def main():
    global visited, A, C, R
    C, R = map(int, read().rstrip().split())
    A = []
    for i in range(R):
        temp = list(read().rstrip())
        A.append(temp)
    node = []
    s = ''
    e = ''
    dic_node = {}

    for r in range(R):
        for c in range(C):
            if A[r][c] == 'X':
                node.append((r,c))
            elif A[r][c] == 'S':
                s = (r,c)
            elif A[r][c] == 'E':
                e = (r,c)
    dic_node[0] = s

    for i,v in enumerate(node, start= 1):
        dic_node[i] = v
    a = len(node)

    dic_node[a+1] = e

    # print(node)
    # print(dic_node)
    #

    graph = [[0 for _ in range(a+2)]for _ in range(a+2)]
    for i in range(a+2):
        graph[i][i] = 0
    #
    for permu in list(permutations(range(a+2),2)):
        visited = [[0 for c in range(C)]for r in range(R)]
        r1, c1 = dic_node[permu[0]]
        r2, c2 = dic_node[permu[1]]
        # print(permu[0],permu[1])
        graph[permu[0]][permu[1]] = bfs(r1,c1,r2,c2)

    for i in range(len(graph)):
        print(graph[i])
    res = 1e9
    for permu in list(permutations(range(1,a+1),a)):
        # print(permu)
        temp = 0
        prev = 0
        end = 0
        for i in permu:
            # print(i)
            temp += graph[prev][i]
            prev = i

        temp += graph[prev][a+1]
        res = min(temp, res)

    print(res)



if __name__ == '__main__':
    main()


