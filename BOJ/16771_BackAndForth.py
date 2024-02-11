first = list(map(int, input().split()))
second = list(map(int, input().split()))
possible = set()

def recursion(first, second, day, total):
    global possible
    if day % 2 == 0:
        for bucket in set(first):
            nfirst = first.copy()
            nsecond = second.copy()
            # first 에서 빼서 second에 더함
            nfirst.remove(bucket)
            nsecond.append(bucket)
            recursion(nfirst, nsecond, day+1, total-bucket)
    else:
        for bucket in set(second):
            nfirst = first.copy()
            nsecond = second.copy()
            # second에서 빼서 first에 더함 
            nsecond.remove(bucket)
            nfirst.append(bucket)
            # 마지막 날은 결과에 추가
            if day == 3:
                possible.add(total+bucket)
            else:
                recursion(nfirst, nsecond, day+1, total+bucket)

recursion(first, second, 0, 1000)
print(len(possible))
