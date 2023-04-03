import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():

    Pa,dak = map(int, read().rstrip().split())
    Pa_len = [int(read()) for _ in range(Pa)]
    lo = 1
    hi = max(Pa_len)
    res = 0
    while lo <= hi:
        mid = (lo+hi)//2  #단위 길이
        N = 0 #쓸파의 개수
        # res = 0 # 나머지 파
        for i in Pa_len:
            N += i //mid
        # print(mid, N, res)
        if N >= dak:  #단위 길이를 늘여야지
            lo = mid + 1
            res = mid
        elif N < dak:
            hi = mid -1
        # print(lo,hi)
    print(sum(Pa_len) - res*dak)

if __name__ == '__main__':
    main()


