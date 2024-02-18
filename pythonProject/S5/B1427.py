N = input()

N_list = list(N)

N_list.sort(reverse=True)
print(*N_list,sep='')