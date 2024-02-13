word_list = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()
    if word == '#':
        break
    word = word.lower()
    count = 0
    for char in word:
        if char in word_list:
            count += 1
    print(count)