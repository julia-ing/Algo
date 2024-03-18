def solution(msg):
    dictionary = {}
    for num in range(0, 26):
        dictionary[chr(num + 65)] = num + 1

    answer = []
    plus = 1
    s = 0
    while True:
        if s == len(msg):
            break
        # 사전에 있는 가장 긴 문자열 찾기
        e = len(msg)
        while e >= s:
            if msg[s:e] in dictionary:
                break
            else:
                e -= 1
        answer.append(dictionary[msg[s:e]])
        dictionary[msg[s:e+1]] = 26 + plus
        plus += 1
        s += len(msg[s:e])     
        
    return answer