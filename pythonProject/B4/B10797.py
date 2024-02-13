day = int(input())
car_list = list(map(int, input().split()))

count = 0
for car in car_list:
    if car == day:
        count += 1

print(count)