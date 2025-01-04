first = input()
second = input()
third = input()

answer = ''

if first != 'Fizz' and first != 'Buzz' and first != 'FizzBuzz':
    answer = int(first) + 3

elif second != 'Fizz' and second != 'Buzz' and second != 'FizzBuzz':
    answer = int(second) + 2

else:
    answer = int(third) + 1

if answer % 3 == 0 and answer % 5 == 0:
    answer = 'FizzBuzz'

elif answer % 3 == 0:
    answer = 'Fizz'

elif answer % 5 == 0:
    answer = 'Buzz'

print(answer)

