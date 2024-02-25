N = int(input())
time = []

for _ in range(N):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))

res = 1
now = time[0][1]
for i in range(1, N):
    if time[i][0] >= now:
        now = time[i][1]
        res += 1

print(res)