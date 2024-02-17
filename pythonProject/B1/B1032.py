N = int(input())
base_file = list(map(str, input()))
answer = base_file[:]
for i in range(1, N):
    file = list(map(str, input()))
    for j in range(len(base_file)):
        if base_file[j] == file[j] and answer[j] != '?':
            answer[j] = base_file[j]
        else:
            answer[j] = '?'

print(*answer, sep='')