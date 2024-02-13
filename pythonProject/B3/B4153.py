while True:
    abc_list = list(map(int, input().split()))
    abc_list.sort()
    if abc_list[0] == 0 and abc_list[1] == 0 and abc_list[2] == 0:
        break
    if abc_list[0] ** 2 + abc_list[1] ** 2 == abc_list[2] ** 2:
        print('right')
    else:
        print('wrong')