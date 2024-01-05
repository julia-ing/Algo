def solution(s):
    stack = []
    
    if s[0] == ')':
        return False
    
    for b in s:
        stack.append(b)
        if b == ')' and len(stack) >= 2:
            stack.pop(-1)
            stack.pop(-1)
    
    if stack:
        return False

    return True