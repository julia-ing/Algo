import sys
name = sys.stdin.readline().rstrip()

count_dict = {}

for s in name:
    count_dict[s] = name.count(s)

center = ''
for k,v in count_dict.items():
    if v % 2 == 1:
        if len(center)>0:
            print("I'm Sorry Hansoo")
            exit(0)
        center = k


ans = ''
for k, v in sorted(count_dict.items()):
    ans += k * (v//2)
ans += center + ans[::-1]
print(ans)