import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def main():
    R,C = map(int, read().rstrip().split())
    a = []
    b = [[-1 for _ in range(C)]for _ in range(R)]
    for i in range(R):
        temp = list(read().rstrip())
        a.append(temp)

    # print(a)

    for r in range(R):
        flag = 0
        cnt = 1
        for c in range(C):
            if a[r][c] == 'c':
                b[r][c] = 0
                flag = 1
                cnt = 1
            else:
                if flag == 0:
                    b[r][c] = -1
                else:
                    b[r][c] = cnt
                    cnt += 1

    for i in range(R):
        for j in range(C):
            print(b[i][j], end = ' ')
        print()

if __name__ == '__main__':
    main()