def check_bingo():
    bingo_count = 0

    for i in range(5):
        _sum = 0
        for j in range(5):
            _sum += bingo_list[i][j]
        if _sum == 0:
            bingo_count += 1
        if bingo_count == 3:
            return bingo_count

    for i in range(5):
        _sum = 0
        for j in range(5):
            _sum += bingo_list[j][i]
        if _sum == 0:
            bingo_count += 1
        if bingo_count == 3:
            return bingo_count

    _sum = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                _sum += bingo_list[i][j]
    if _sum == 0:
        bingo_count += 1
    if bingo_count == 3:
        return bingo_count

    _sum = 0
    for i in range(5):
        for j in range(5):
            if i + j == 4:
                _sum += bingo_list[i][j]
    if _sum == 0:
        bingo_count += 1
    if bingo_count == 3:
        return bingo_count


bingo_list = [list(map(int, input().split())) for _ in range(5)]

call_list = [list(map(int, input().split())) for _ in range(5)]

count = 0
flag = False

for i in range(5):
    for j in range(5):
        for m in range(5):
            for n in range(5):
                if call_list[i][j] == bingo_list[m][n]:
                    bingo_list[m][n] = 0
                    count += 1
        if check_bingo() == 3:
            print(count)
            flag = True
            break
    if flag:
        break