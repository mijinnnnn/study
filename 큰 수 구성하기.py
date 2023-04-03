import sys
from itertools import *

read = sys.stdin.readline

def main():
    N, K = map(int, read().rstrip().split())
    N = str(N)
    N_li = [int(i) for i in N]
    # print(N_li)
    A = list(map(int, read().rstrip().split()))
    A.sort()
    A.reverse()
    for y in range(len(N_li),0, -1):
        # print(y)
        for i in list(product(A, repeat = y)):
            i = list(map(str, i))
            j = int(''.join(i))
            # print(j)
            if j <= int(N):
                print(j)
                return

if __name__ == '__main__':
    main()