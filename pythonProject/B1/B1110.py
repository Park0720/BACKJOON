N = int(input())
num = N
a = 0
count = 0
if N == 0:
    count = 1
while True:
    num_list = []
    if a == N:
        break
    while num > 0:
        num_list.append(num % 10)
        num = num // 10
    a = ((num_list[0] % 10) * 10) + (sum(num_list) % 10)
    num = a
    count += 1
print(count)