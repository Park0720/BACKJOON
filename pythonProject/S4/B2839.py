N = int(input())

count = 0
while N > 0:
    N -= 5
    count += 1
    if N % 3 == 0:
        break

while N > 0:
    N -= 3
    count += 1

print(count, N)