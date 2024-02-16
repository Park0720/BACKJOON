while True:
    num_list = list(map(int, input()))
    if num_list == [0]:
        break
    reversed_num_list = num_list[::-1]

    if num_list == reversed_num_list:
        print('yes')
    else:
        print('no')