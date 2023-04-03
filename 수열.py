import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N,K = map(int, read().rstrip().split())
    A = list(map(int, read().rstrip().split()))
    r_res = int(sum(A[0:K]))
    res = int(sum(A[0:K]))
    for i in range(K,N):
        res = res - A[i-K] + A[i]
        if A[i-K] < A[i]:
            r_res = max(r_res, res)
    print(r_res)

if __name__ == '__main__':
    main()