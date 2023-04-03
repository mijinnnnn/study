from collections import deque
import time
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    s = list(read().rstrip())
    bomb = list(read().rstrip())
    a = len(bomb)
    stack = []
    for i in s:

        stack.append(i)
        # print(stack[-a:], bomb)
        if len(stack) >= a and stack[-1] == bomb[-1]:
            if stack[-a:] == bomb:
                for _ in range(a):
                    stack.pop()

    # print(s)
    if len(stack)==0 :
        print('FRULA')
    else:
        print(''.join(stack))


if __name__ == '__main__':
    main()


