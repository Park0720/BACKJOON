N, K = map(int, input().split())

num_list = list(range(1, N+1))
answer = []

i = K-1
while len(num_list) > 0:

    answer.append(num_list[i])
    num_list.pop(i)
    if not num_list:
        break
    i += K-1
    if i >= len(num_list):
        i %= len(num_list)

print('<', end='')
print(*answer, sep=', ', end='')
print('>')