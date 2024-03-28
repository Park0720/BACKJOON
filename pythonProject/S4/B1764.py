N, M = map(int, input().split())

name_dict = {}
for i in range(N):
    N_name = input()
    name_dict[N_name] = N_name

name_list = []
for j in range(M):
    M_name = input()
    if name_dict.get(M_name):
        name_list.append(name_dict.get(M_name))

name_list.sort()

print(len(name_list))
print(*name_list, sep='\n')
