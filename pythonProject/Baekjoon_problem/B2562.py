lst = []
for i in range(9):
    lst.append(int(input()))
new_lst = sorted(lst)
print(new_lst[8])
x = lst.index(new_lst[8])
print(x + 1)