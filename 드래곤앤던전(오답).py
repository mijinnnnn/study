
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    N,atk = map(int, read().rstrip().split())

    res = 1
    flag = 0
    for i in range(N):
        t, a, h = map(int, read().rstrip().split())
        if t == 2:
            flag = 0
            atk += a
            res -= h


        elif t == 1:
            flag = 1
            temp = h//atk
            temp_na = h%atk
            # print(temp)
            if temp_na == 0:
                res += (temp-1)*a
            else:
                res += (temp+1)*a

    print(res)




if __name__ == '__main__':
    main()


