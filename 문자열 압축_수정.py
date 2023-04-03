def solution(s):

    s_li = list(str(s))
    answer = len(s)
    for i in range(1,len(s)):
        res = []
        out_j = 0
        cnt = 1
        temp = s_li[0:i]
        for j in range(1,len(s)-i,i):
            out_j = j
            if temp == s_li[j:j+i]:
                cnt += 1
            else:
                res.append(cnt)
                res.append(temp)
                temp = s_li[j:j+i]
                cnt = 1
        res.append(cnt)
        res.append(temp)
        res.append(s[out_j+i:])
        while 1 in res:
            res.remove(1)

        result =''
        for i in res:
            result += str(i)


        answer = min(answer, len(result))

    return answer