base_list = [list(map(str, input())) for _ in range(5)]

for i in range(15):
    for j in range(5):
        try:
            print(base_list[j][i], end='')
        except:
            continue