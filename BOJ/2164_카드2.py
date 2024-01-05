from collections import deque
n = int(input())

card = deque()
for i in range(n):
    card.append(i+1)

while len(card) > 1:
    card.popleft()
    last = card.popleft()
    card.append(last)

print(card[0])