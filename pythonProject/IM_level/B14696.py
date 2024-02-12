N = int(input())

for i in range(N):
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_count_list = [0] * 5
    for j in range(1, len(a_list)):
        a_count_list[a_list[j]] += 1
    b_count_list = [0] * 5
    for k in range(1, len(b_list)):
        b_count_list[b_list[k]] += 1

    for m in range(4, 0, -1):
        if a_count_list[m] > b_count_list[m]:
            print('A')
            break
        elif a_count_list[m] == b_count_list[m]:
            if m == 1:
                print('D')
                break
            continue
        else:
            print('B')
            break