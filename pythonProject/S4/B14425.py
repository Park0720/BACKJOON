import sys

N, M = map(int, sys.stdin.readline().strip().split())

word_dict = {}
for i in range(N):
    word = sys.stdin.readline().strip()
    word_dict[word] = word

count = 0

for i in range(M):
    word = sys.stdin.readline().strip()
    if word_dict.get(word):
        count += 1

print(count)