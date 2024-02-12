word = input()
word = word.upper()

count_list = [0] * 26
max_count = 0
_max = 0
max_idx = 0
for i in word:
    count_list[ord(i) - 65] += 1

for j in range(len(count_list)):
    if count_list[j] > _max:
        max_idx = j
        _max = count_list[j]

for k in count_list:
    if k == _max:
        max_count += 1

if max_count > 1:
    print('?')
else:
    print(chr(max_idx + 65))