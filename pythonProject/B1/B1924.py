day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


x, y = map(int, input().split())

answer = 0
if x == 1:
    answer += y-1
elif y == 1:
    pass
else:
    answer += y-1

for i in range(0, x-1):
    if x == 1:
        answer += month[i] - 1
    else:
        answer += month[i]

print(day[answer % 7])