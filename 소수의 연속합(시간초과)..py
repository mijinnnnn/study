from collections import deque
import time
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def print_(A):
    for i in range(len(A)):
        print(A[i])
def main():
    start = time.time()
    N = int(read().rstrip())
    res = [i for i in range(2,N+1)]   #400만
    i = 0
    cnt = 0
    while i < len(res):
        div = res[i]
        if div == N:
            cnt += 1
        for k in res:
            if k != div and k%div == 0:
                res.remove(k)

        i += 1

    # print(res)

    s = 0
    e = 2
    sum_so = res[0] + res[1]
    while e < len(res):
        if sum_so < N:
            sum_so += res[e]
            e += 1
        elif sum_so > N:
            sum_so -= res[s]
            s += 1
        else:
            cnt += 1
            sum_so += res[e]
            e += 1
        # print(sum_so)

    print(cnt)
    end = time.time()

    print(end - start)

if __name__ == '__main__':
    main()


