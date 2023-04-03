from collections import deque

receive = [1,0,3,2]

pipe = [[],[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]
pipe_R = [[0,0,0,0],[-1,1,0,0],[-1,1,0,0], [0,0,0,0], [-1,0,0,0],[0,1,0,0],[0,1,0,0],[-1,0,0,0]]
pipe_C = [[0,0,0,0],[0,0,-1,1],[0,0,0,0], [0,0,-1,1], [0,0,0,1],[0,0,0,1],[0,0,-1,0],[0,0,-1,0]]

def bfs():
    global A,visited,R,C,L,rs,cs,res
    Q = deque()
    Q.append((rs,cs,1))
    visited[rs][cs] = 1
    while Q:
        r = Q[0][0]
        c = Q[0][1]
        time = Q[0][2]
        Q.popleft()

        for i in range(4):
            nr = r + pipe_R[A[r][c]][i]
            nc = c + pipe_C[A[r][c]][i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0:
                continue

            if receive[i] not in pipe[A[nr][nc]]:
                continue
            # if receive[i] not in pipe[A[nr][nc]]:
            #     continue
            if time >= L:
                continue
            # print(nr,nc)
            visited[nr][nc] = 1
            Q.append((nr,nc,time+1))
            res += 1

def solve():
    global A,visited,R,C,L,rs,cs,res
    R, C, rs, cs, L = map(int, input().split())
    A = []
    visited = [[0 for _ in range(C)]for _ in range(R)]
    for i in range(R):
        A.append(list(map(int, input().split())))
    res = 1
    bfs()
    return res

def main():
    test = int(input())

    for i in range(1,test+1):
        print(f'#{i} {solve()}')

if __name__ == '__main__':
    main()