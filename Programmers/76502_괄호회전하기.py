def solution(s):
    answer = 0
    def is_valid(s):
        stack = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack == []:
                    return False
                target = stack.pop()
                if c == ')' and target != '(':
                    return False
                if c == ']' and target != '[':
                    return False
                if c == '}' and target != '{':
                    return False
        if stack:
            return False
        return True
    
    for _ in range(len(s)):
        s = list(s)
        first = s.pop(0)
        s.append(first)
        if is_valid(s):
            answer += 1
    return answer