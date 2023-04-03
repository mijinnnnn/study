import sys
read = sys.stdin.readline
global N, M, a, res

def check(mid):
    global N, M, a, res
    sum = 0

    for i in a:
        # 절단기 높이가 더 높으면 나무가 안잘림. 음수값이 나와 잘못된 결과 도출
        if mid >= i:
            continue
        sum += i - mid

    # 자른 길이는 M은 되어야 함
    return sum >= M


def main():
    global N, M, a, res
    N, M = map(int, read().rstrip().split())
    a = list(map(int, read().rstrip().split()))

    lo = 0
    hi = max(a) # 나무 최대 높이를 기준으로 잡으면 하나도 안잘리기 때문에 기준으로 잡음

    while lo <= hi:
        # 절단기의 높이.
        mid = (lo + hi) // 2

        # 길이가 M 만큼 확보 된 경우. 우리는 이 중에 최소값을 원함. 최소가 되려면 절단기 높이가 최대가 되어야 함
        if check(mid):
            lo = mid + 1
            res = mid
        else:   # 길이가 M 만큼 확보 안된 경우. 더 많이 자르려면 높이를 낮춰야 됨.
            hi = mid - 1

    print(res)


if __name__ == '__main__':
    main()