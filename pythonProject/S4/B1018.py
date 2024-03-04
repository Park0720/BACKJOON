N, M = map(int, input().split())

base_list = [list(map(str, input())) for _ in range(N)]

min_diff = 999999999999
row, col = 0, 0

for i in range(N-7):
    for j in range(M-7):
        b_count = 0
        w_count = 0
        for m in range(8):
            for n in range(8):
                if base_list[i+m][j+n] == 'B':
                    b_count += 1
                elif base_list[i+m][j+n] == 'W':
                    w_count += 1
        print(b_count, w_count)
        diff = abs(b_count - w_count)
        if min_diff > diff:
            min_diff = diff

print(min_diff)