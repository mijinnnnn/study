import sys
read = sys.stdin.readline

def main():
    # 알파뱃을 셀 배열. 알파뱃이 26개 이므로.
    counting = [0 for _ in range(26)]
    S = read().rstrip()

    for i in S:
        counting[ord(i) - ord('a')] += 1

    for i in counting:
        print(i, end=' ')


if __name__ == '__main__':
    main()