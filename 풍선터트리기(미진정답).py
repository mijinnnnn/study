import sys
read = sys.stdin.readline

def main():
    N = int(read().rstrip())
    a = list(map(int, read().rstrip().split()))

    cur_idx = 0
    res = []
    valid_idx = N

    for _ in range(N):
        res.append(cur_idx+1)
        move = a[cur_idx]
        a[cur_idx] = 0
        cnt = 0
        valid_idx -= 1
        if valid_idx == 0:
            break

        if move > 0:
            while cnt != abs(move):
                cur_idx = (cur_idx +1)%N
                if a[cur_idx] == 0:
                    continue
                cnt += 1
        else:
            while cnt != abs(move):
                cur_idx = (cur_idx -1)%N
                if a[cur_idx] == 0:
                    continue
                cnt += 1
    print(*res)

if __name__== '__main__':
    main()