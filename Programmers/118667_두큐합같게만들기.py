from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1Sum = sum(queue1)
    q2Sum = sum(queue2)
    
    limit = (len(queue1)) * 3
    
    if (q1Sum + q2Sum) % 2 != 0:
        return -1
    
    while True:
        if q1Sum == q2Sum:
            break
        elif q1Sum > q2Sum: 
            tmp = q1.popleft()
            q1Sum -= tmp
            q2Sum += tmp
            q2.append(tmp)
            answer += 1
        else:
            tmp = q2.popleft()
            q2Sum -= tmp
            q1Sum += tmp
            q1.append(tmp)
            answer += 1
        
        if answer == limit:
            answer = -1
            break

    return answer
