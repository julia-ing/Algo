hour = int(input())

# 00:00:00 ~ n:59:59 까지 중 3이 하나라도 포함: +1
count = 0
for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
