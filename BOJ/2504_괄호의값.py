brackets = list(input())

total = 1
stack = []
res = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
        total *= 2
    elif brackets[i] == '[':
        stack.append(brackets[i])
        total *= 3
    elif brackets[i] == ')':
        if not stack or stack[-1] != '(':  # 올바르지 못한 경우 
            res = 0
            break
        if brackets[i-1] == '(':  # 누적 계산
            res += total
        total //= 2
        c = stack.pop() # ] 로 시작될 수 있기 때문에 pop을 나중에 해줘야 함
    else:
        if not stack or stack[-1] != '[':
            res = 0
            break
        else:
            if brackets[i-1] == '[':
                res += total
            total //= 3
        c = stack.pop()
    print(brackets[i], stack, total, res)

if stack:
    print(0)
    exit(0)
else:
    print(res)                
