N = int(input())
lst = list(map(int, input().split()))
v = int(input())
count = 0
for i in lst:
    if v == i:
        count += 1
print(count)