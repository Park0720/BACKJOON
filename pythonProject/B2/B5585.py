money = [500, 100, 50, 10, 5, 1]

N = int(input())
count = 0
N = 1000 - N
for val in money:
    if val <= N:
        count += N // val
        N %= val

print(count)