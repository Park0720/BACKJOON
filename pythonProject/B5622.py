word = input()
word_dict ={
    'ABC': 2,
    'DEF': 3,
    'GHI': 4,
    'JKL': 5,
    'MNO': 6,
    'PQRS': 7,
    'TUV': 8,
    'WXYZ': 9,
}

time = 0

for char in word:
    for key in word_dict:
        for k in key:
            if char == k:
                time += word_dict.get(key) + 1
print(time)