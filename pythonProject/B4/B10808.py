alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_count = [0] * 26

word = input()

for i in range(len(alphabet_list)):
    for j in range(len(word)):
        if alphabet_list[i] == word[j]:
            alphabet_count[i] += 1

print(*alphabet_count)