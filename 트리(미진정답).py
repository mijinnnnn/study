import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, A):
    if not A[x]:
        return 1

    count = 0
    for i in A[x]:
        count += dfs(i, A)
    return count

def main():
    n = int(read().rstrip())
    temp = list(map(int, read().rstrip().split()))
    d = int(read().rstrip())
    A = [[] for _ in range(n)]
    root = -1

    for i in range(n):
        if temp[i] == -1:
            root = i
        elif temp[i] == d or i == d:
            continue
        else:
            A[temp[i]].append(i)

    # if root == -1: #루트 노드가 없는 경우
    #     print(0)
    if d == root:
        print(0)
    else:
        print(dfs(root, A))

if __name__ == '__main__':
    main()