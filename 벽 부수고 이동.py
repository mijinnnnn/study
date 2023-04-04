
from collections import deque
import sys
read = sys.stdin.readline

global R, C, a, visited
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global R, C, a, visited
    Q = deque([(0, 0, 1)])  # 행, 열, 남은 벽 부수기 횟수
    visited[0][0][1] = 1

    while len(Q) > 0:
        r, c, wall = Q.popleft()

        if r == R - 1 and c == C - 1:
            return visited[r][c][wall]  # 시작 칸과 도착 칸도 포함해서 세야 함

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 벗어나는지 체크
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            # 벽이 아닌데 방문하지 않은 경우
            if a[nr][nc] == 0 and visited[nr][nc][wall] == 0:
                Q.append((nr, nc, wall))
                visited[nr][nc][wall] = visited[r][c][wall] + 1
            # 벽인데 아직 벽 부수기 사용 안한 경우
            elif a[nr][nc] == 1 and wall != 0 and visited[nr][nc][wall - 1] == 0:
                Q.append((nr, nc, wall - 1))
                visited[nr][nc][wall - 1] = visited[r][c][wall] + 1

    # bfs 끝날 때 까지 return 안했으면 못가는 경우
    return -1

def main():
    global R, C, a, visited
    R, C = map(int, read().rstrip().split())
    visited = [[[0 for _ in range(2)] for _ in range(C)] for _ in range(R)]  # [행][열][남은 벽 부수기 횟수]
    a = []

    for _ in range(R):
        c = list(map(int, read().rstrip()))
        a.append(c)
    print(visited)

    print(bfs())
    print(visited)

if __name__ == '__main__':
    main()




