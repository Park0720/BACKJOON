from collections import deque

N = int(input())

deck = deque()
for i in range(1, N+1):
    deck.append(i)
while len(deck) > 1:
    abandon = deck.popleft()
    change = deck.popleft()
    deck.append(change)

print(deck[0])