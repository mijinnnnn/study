from collections import deque
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    a = deque([1,3,5,6,7,8])

    a.rotate(2)
    print(a)



if __name__ == '__main__':
    main()


