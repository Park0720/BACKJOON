N = int(input())

count = 0
for i in range(1, N+1):
    if i <= 99:
        count += 1
        continue
    elif i > 99:
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            count += 1

print(count)