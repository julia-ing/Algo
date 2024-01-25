n = int(input())
s = list(map(int, input().split()))

a = [0] * n  # 부분합 배열
m = [0] * n  # 배열 뒤에서부터 누적 최소값 저장

a[-1] = m[-1] = s[-1]
for i in range(n - 2, -1, -1):
    a[i] = a[i + 1] + s[i]
    m[i] = min(s[i], m[i + 1])

# # 1차 시도: 오답, 이유: avg가 실수 형태이기 때문에 오차가 생김
# val = []
# max = 0
# for k in range(n-1):
#     avg = (a[k] - m[k]) / (n-k-1)
#     if avg > max:
#         max = avg
#         val = []
#         val.append(k)
#     elif avg == max:
#         val.append(k)
# for v in val:
#     print(v)

# 실수값인 avg 가 아닌 sum 과 cnt 를 따로 저장해서 계산
max_avg = (0, 1)  # (sum, cnt)
for k in range(1, n - 1):
    # a[k] - m[k] / (n - k - 1) > max_avg
    if (a[k] - m[k]) * max_avg[1] > max_avg[0] * (n - k - 1):
        max_avg = (a[k] - m[k], n - k - 1)

for k in range(1, n - 1):
    # a[k] - m[k] / (n - k - 1) == max_avg
    if (a[k] - m[k]) * max_avg[1] == max_avg[0] * (n - k - 1):
        print(k)
