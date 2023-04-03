from collections import deque
import time
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N, d, k , c = map(int, read().rstrip().split())
    # print(N, d, k, c)

    cnt = 1
    counting = [0 for i in range(d+1)] # 0~d 까지 배열 0 초기
    li = []
    for i in range(N):
        # print('i=',  i)
        t = int(read().rstrip())
        li.append(t)
        counting[t] += 1
        # print(counting)
        if i < k:
            if t != c and counting[t] == 1:
                cnt += 1
        else:
            counting[li[i-k]] -= 1
            # print(li[i - k])
            # print(counting[li[i-k]])
            if li[i-k] != c and counting[li[i-k]] <=0:
                cnt -= 1
            if t != c and counting[t] == 1:
                cnt += 1

        # print(t)
        # print(counting[t])
        # print(cnt)
    print(cnt)

if __name__ == '__main__':
    main()


