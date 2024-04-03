word = input()

# '-' 연산은 가장 마지막에 하려고
word_list = word.split('-')

# print(word_list)

# '-'를 기점으로 나눈 리스트를 '+'로 다시 나눠 줌
for i in range(len(word_list)):
    word_list[i] = word_list[i].split('+')

# print(word_list)

# 총 합계
outer_sum = 0

# 스플릿한 word_list 순회
for i in range(len(word_list)):
    # 모두 int로 변경
    word_list[i] = list(map(int, word_list[i]))
    inner_sum = 0

    # 만약에 리스트 길이가 2이상이면 내부에 +가 있었다는 것
    # 하지만 '-'가 없는 경우 혹은 리스트의 가장 처음인 경우 합을 더 해줌
    if len(word_list[i]) >= 2 and i == 0:
        inner_sum = sum(word_list[i])
        outer_sum += inner_sum

    # +가 있는 부분을 모두 뺀다면 연산의 최솟값이 됨
    elif len(word_list[i]) >= 2:
        inner_sum = sum(word_list[i])
        outer_sum -= inner_sum

    # 만약 리스트의 길이가 1이라면 내부에 +가 없었음
    # 하지만 리스트의 가장 처음인 경우 합을 더 해줌
    elif len(word_list[i]) == 1 and i == 0:
        inner_sum = sum(word_list[i])
        outer_sum += inner_sum

    # 가장 처음이 아닌 경우 합에서 빼줌
    elif len(word_list[i]) == 1:
        inner_sum = sum(word_list[i])
        outer_sum -= inner_sum

print(outer_sum)
