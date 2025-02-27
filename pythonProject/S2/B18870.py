import sys

N = int(sys.stdin.readline())

line = list(map(int, sys.stdin.readline().split()))
sort_list = sorted(set(line))
dic = {y : x for x, y in enumerate(sort_list)}

for i in line:
    print(dic[i], end= ' ')

print()