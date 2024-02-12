num_list = []
for i in range(10):
    a = int(input())
    num_list.append(a % 42)

print(len(set(num_list)))