C = int(input())

for test_case in range(1, C+1):
    grade_list = list(map(int, input().split()))
    grade_list.pop(0)
    avg = sum(grade_list)/len(grade_list)
    count = 0
    for grade in grade_list:
        if grade > avg:
            count += 1

    persent = count * 100 / len(grade_list)

    print(f'{persent:.3f}%')