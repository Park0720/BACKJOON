A, B, C = map(int, input().split())
D = int(input())

second = C + D % 60

minute = B + D // 60

hour = A

if second >= 60:
    minute += second // 60
    second %= 60

if minute >= 60:
    hour += minute // 60
    minute %= 60

if hour >= 24:
    hour = hour % 24
print(hour, minute, second)