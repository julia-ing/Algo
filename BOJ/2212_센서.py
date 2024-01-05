N = int(input()) # 센서
K = int(input()) # 집중국

sensor = list(map(int, input().split()))
sensor.sort()

dist = []
for i in range(N-1):
    dist.append(sensor[i+1] - sensor[i])

dist.sort()
print(sum(dist[:N-K]))