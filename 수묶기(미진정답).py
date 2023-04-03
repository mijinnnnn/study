from collections import deque
import time
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def print_(A):
    for i in range(len(A)):
        print(A[i])
def calc(A):
    global sum,zero

    if len(A) == 1:
        if A[0] < 0 and zero != 0:
            sum = sum
            zero -= 1
        else:
            sum += A[0]
        # print(sum)
        return
    elif len(A) % 2 == 0:
        for i in range(0,len(A)-1, 2):
            sum += A[i] * A[i + 1]


    else:
        for i in range(0, len(A), 2):
            if i + 1 == len(A):
                if A[i] < 0 and zero != 0:
                    sum = sum
                    zero -= 1
                else:
                    sum += A[i]
            else:
                sum += A[i] * A[i + 1]


def main():
    global sum,zero
    N = int(read().rstrip())
    minus = []
    plus = []
    zero = 0
    one = 0

    for i in range(N):
        a = int(read().rstrip())
        if a < 0:
            minus.append(a)
        elif a > 1:
            plus.append(a)
        elif a == 1:
            one += 1
        else:
            zero += 1
    sum = 0
    sum += one

    minus.sort()
    plus = sorted(plus, key = lambda x: -x)

    if len(plus) == 0 and len(minus) == 0:
        print(sum)
        return

    if minus:
        calc(minus)
    if plus:
        calc(plus)

    print(minus)
    print(plus)
    print(one)
    print(sum)
if __name__ == '__main__':
    main()


