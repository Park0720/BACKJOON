N, B = map(int, input().split())
a = 10000
num_list = []

while N > 0:
    a = N % B
    N //= B
    num_list.append(a)

num_list = num_list[::-1]

for i in range(len(num_list)):
    if num_list[i] >= 10:
        print(chr(num_list[i] + 55), end='')
    else:
        print(num_list[i], end='')