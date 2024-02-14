N = int(input())

num_list = list(map(int,input().split()))

num_list.sort()

count = 0
for num in num_list:
    num_div_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            num_div_list.append(i)
    if len(num_div_list) == 2:
        count += 1

print(count)