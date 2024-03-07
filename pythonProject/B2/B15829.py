L = int(input())
word = input()

_sum = 0
_hash = 31
for i in range(L):
    _sum += (ord(word[i]) - 96) * _hash ** i

print(_sum % 1234567891)