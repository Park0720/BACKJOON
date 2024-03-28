N, K = map(int, input().split())

coin_list = []
for i in range(N):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

count = 0

for i in range(N):
    if coin_list[i] <= K:
        count += K // coin_list[i]
        K %= coin_list[i]

print(count)