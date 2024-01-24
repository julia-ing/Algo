N = int(input())

info = []
for _ in range(N):
    day, name, num = input().split()
    info.append((int(day), name, int(num)))

info.sort()

milk = [7, 7, 7]
curr_max = [0, 1, 2] # max 저장, 초기에는 동점
res = 0
for day, name, num in info:
    if name == "Bessie":
        milk[0] += num
    elif name == "Elsie":
        milk[1] += num
    else:
        milk[2] += num
    
    new_max = []
    for i in range(3):
        if max(milk) == milk[i]:
            new_max.append(i)
    if new_max != curr_max:
        res += 1
        curr_max = new_max

print(res)
