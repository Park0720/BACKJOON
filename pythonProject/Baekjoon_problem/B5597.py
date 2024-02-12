num_list = []

not_list = []
for i in range(1, 29):
    a = int(input())
    num_list.append(a)

for i in range(1, 31):
    if i not in num_list:
        not_list.append(i)

sorted_list = sorted(not_list)

print(sorted_list[0])
print(sorted_list[1])