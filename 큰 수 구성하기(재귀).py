import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


global a, res, N, K


def recursive(x):
    global a, res, N, K
    if N < x:   # N 보다 작거나 같은 자연수 중 가장 큰 수를 찾는 것이 목적. x가 더 크면 위배
        return
    # N을 넘는 경우는 이제 없음. 지금까지 나온 수 중 가장 큰 수로 res 갱신
    print(x)
    res = max(res, x)

    for i in a:
        recursive(x * 10 + i)   # 1의 자리에 a 원소 하나 넣어서 위의 작업 반복


def main():
    global a, res, N, K
    N, K = map(int, read().rstrip().split())
    a = list(map(int, read().rstrip().split()))
    res = -1    # 최댓값 구하는 문제. 자연수 구하는 문제이므로 -1보다는 무조건 큼

    recursive(0)
    print(res)


if __name__ == '__main__':
    main()