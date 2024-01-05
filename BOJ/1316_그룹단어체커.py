# https://www.acmicpc.net/problem/1316
n = int(input())
res = n
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:  # 연달아 같은 문자면 패스
            pass
        elif word[j] in word[j+1:]:  # 다음 문자와 다른 문자이면서 이후에 해당 문자가 발견되는 경우
            res -= 1
            break

print(res)
