# https://www.acmicpc.net/problem/1043

n, m = map(int, input().split())
res = 0
truth_ppl_list = set(input().split()[1:])
party_ppl_list = []
for i in range(m):
    party_ppl_list.append(set(input().split()[1:]))
for i in range(m):
    for party_ppl in party_ppl_list:
        if party_ppl & truth_ppl_list:
            truth_ppl_list = truth_ppl_list.union(party_ppl)

for party_ppl in party_ppl_list:
    if party_ppl & truth_ppl_list:
        continue
    res += 1

print(res)
