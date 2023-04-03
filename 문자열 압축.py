def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        cnt = 1
        word = ''
        res = ''
        for j in range(0, len(s), i):
            if len(s) % i == 0:
                if j + 2 * i == len(s) - i:

                    if str(s[j:j + i]) == str(s[j + i:j + 2 * i]):
                        cnt += 1
                        res += str(cnt) + str(s[j:j + i])
                    else:
                        res += str(s[j:j + i]) + str(s[j + i:j + 2 * i])

                elif str(s[j:j + i]) == str(s[j + i:j + 2 * i]):
                    cnt += 1
                    # temp = str(s[j+i:j+2*i])
                elif str(s[j:j + i]) != str(s[j + i:j + 2 * i]):
                    if cnt != 1:
                        res += str(cnt) + str(s[j:j + i])
                        cnt = 1
                    else:
                        res += str(s[j:j + i])

            elif len(s) % i != 0:
                if j + 2 * i == len(s) - i:
                    if str(s[j:j + i]) == str(s[j + i:j + 2 * i]):
                        cnt += 1
                        res += str(cnt) + str(s[j:j + i]) + str(s[j + 2 * i + 1:])
                    else:
                        res += str(s[j:j + i]) + str(s[j + i:j + 2 * i]) + str(s[j + 2 * i + 1:])

                elif str(s[j:j + i]) == str(s[j + i:j + 2 * i]):
                    cnt += 1
                    # temp = str(s[j+i:j+2*i])
                elif str(s[j:j + i]) != str(s[j + i:j + 2 * i]):
                    if cnt != 1:
                        res += str(cnt) + str(s[j:j + i])
                        cnt = 1
                    else:
                        res += str(s[j:j + i])
        print(res)
        answer = min(answer, len(res))

    return answer