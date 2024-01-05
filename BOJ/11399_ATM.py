# https://www.acmicpc.net/problem/11399
n = int(input())
num_list = list(map(int, input().split(' ')))
num_list = sorted(num_list)
res = 0
for i in range(1, n+1):
    res += sum(num_list[:i])

print(res)
