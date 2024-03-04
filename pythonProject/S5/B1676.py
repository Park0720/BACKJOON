def fact(N):
    if N == 1 or N == 0:
        return 1

    return N * fact(N-1)


N = int(input())

word = str(fact(N))
count = 0

for i in range(len(word) - 1, -1, -1):
    if word[i] != '0':
        break
    count += 1

print(count)
