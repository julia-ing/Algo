L, N, rF, rB = map(int, input().split())
rest_stops = []
for i in range(N):
    rest_stops.append(list(map(int, input().split())))

# tastiness 내림차순 정렬
rest_stops.sort(key=lambda x: -x[1])

prev = 0
res = 0
for x, c in rest_stops:
    # Bessie가 뒤쳐지지 않는 경우에만 쉬기
    if prev <= x:
        # 쉴 수 있는 시간 * c
        res += (x-prev) * (rF-rB) * c
        prev = x

print(res)