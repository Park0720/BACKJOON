def status_change(target):
    if target == 0:
        target = 1

        return target

    elif target == 1:
        target = 0

        return target


switch_count = int(input())

switch_status = [0] + list(map(int, input().split()))

student_count = int(input())

for i in range(student_count):
    gender, num = map(int, input().split())

    if gender == 1:
        for j in range(1, switch_count + 1):
            if j % num == 0:
                switch_status[j] = status_change(switch_status[j])

    elif gender == 2:
        end = 0
        if num - 1 < switch_count - num:
            end = num - 1
        else:
            end = switch_count - num
        for j in range(1, end + 1):
            if switch_status[num - j] == switch_status[num + j]:
                switch_status[num - j] = status_change(switch_status[num - j])
                switch_status[num + j] = status_change(switch_status[num + j])
            else:
                break
        switch_status[num] = status_change(switch_status[num])

for i in range(1, switch_count + 1):
    print(switch_status[i], end=' ')
    if i % 20 == 0:
        print()