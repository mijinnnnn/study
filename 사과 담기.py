import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def main():

    N,M = map(int, read().rstrip().split())
    A = int(read())

    s = 1
    e = M+1
    cnt = 0
    for i in range(A):
        apple = int(read().rstrip())
        if apple > e-1:
            cal1 = apple - (e-1)
            cnt += cal1
            s += cal1
            e += cal1
        elif apple < s:
            cal2 = s - apple
            cnt += cal2
            s -= cal2
            e -= cal2
        print(cnt)
    # print(cnt)

if __name__ == '__main__':
    main()