num_list = list(map(int, input()))

count = [0] * 10

for i in num_list:
    count[i] += 1

count_69 = count[6] + count[9]

if count_69 % 2 == 1:
    count_69 += 1
count_69 //= 2

count[6] = 0
count[9] = 0
count.append(count_69)

print(max(count))