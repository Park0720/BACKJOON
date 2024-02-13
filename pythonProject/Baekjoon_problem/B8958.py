T = int(input())

for test_case in range(1, T+1):
    ox_list = list(map(str, input()))
    _sum = 0
    count = 0
    for check in ox_list:
        if check == 'O':
            count += 1
            _sum += count
        else:
            count = 0

    print(_sum)