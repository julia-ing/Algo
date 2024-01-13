N = int(input())

def check(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True

for i in range(N):
    s = input()
    res = check(s)
    if res == True:
        print("YES")
    else:
        print("NO")