num_count = [0] * 10
A = int(input())
B = int(input())
C = int(input())

num = A * B * C

while num > 0:
    num_count[num % 10] += 1
    num = num // 10

for i in range(10):
    print(num_count[i])