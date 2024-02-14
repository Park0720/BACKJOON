N = int(input())

answer = 0
for i in range(1, N):
    a = i
    b = i
    while b > 0:
        a += b % 10
        b //= 10
    if a == N:
        answer = i
        break
print(answer) 