#강사님 코드

import sys
read = sys.stdin.readline


def main():
    stick = read().rstrip()
    stack = []
    res = 0

    for i in range(len(stick)):
        if stick[i] == '(':    # 여는 괄호는 무조건 넣어야 됨.
            stack.append('(')
            continue    # else 쓰면 들여쓰기가 많이 되어서 피하기 위함
        # 이제부터는 닫는 괄호만 생각하면 됨. 문제 특성 상 문자열의 첫번째 문자가 ')' 일 수가 없으므로 고려할 필요 없음
        stack.pop()     # 닫는 괄호가 나오면 pop해야 함. 그래야 레이저일 경우 size만으로 잘린 막대의 개수를 셀 수 있음
        if stick[i - 1] == '(':     # 바로 이전에 여는 괄호가 나왔으면 레이저. 이때는 잘린 막대의 왼쪽을 계산하는 개념
            res += len(stack)
        else:   # 바로 앞이 여는 괄호가 아니기 때문에 막대기가 끝나는 부분. 끝났으므로 +1을 하여 그 막대기에 대한 연산을 마무리
            res += 1

    print(res)


if __name__ == '__main__':
    main()

'''import sys
read = sys.stdin.readline

def main():
    A = list(read().rstrip())
    stack = []
    res = 0
    for i in range(len(A)):
        if len(stack) == 0:
            stack.append(i)
        elif A[stack[-1]] == '(' and A[i] == ')' and i - stack[-1] == 1:
            stack.pop()
            res += len(stack)
        elif A[stack[-1]] == '(' and A[i] == ')' :
            stack.pop()
            res += 1
        else:
            stack.append(i)
    print(res)

if __name__=='__main__':
    main()
'''