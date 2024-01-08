import sys

s = sys.stdin.readline().rstrip()
arr = s.split("-")

minus_list = []
for exp in arr:
    plus_list = exp.split("+")
    tmp = 0
    for c in plus_list:
        tmp += int(c)
    minus_list.append(tmp)

answer = minus_list[0]
if len(minus_list) == 1:
    print(answer)
else:
    for num in range(1, len(minus_list)):
        answer -= minus_list[num]
    print(answer)
