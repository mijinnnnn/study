import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N = int(read().rstrip())
    meetings = []
    for i in range(N):
        s,e = map(int, read().rstrip().split())
        meetings.append((s,e))
    # print(meetings)

    meetings = sorted(meetings, key = lambda x : [x[1],x[0]]) 
    # print(meetings)
    e = meetings[0][0]
    cnt = 0
    for meeting in meetings:
        n_s,n_e = meeting
        # print(n_s,n_e)
        if n_s >= e:
            e = n_e
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()


