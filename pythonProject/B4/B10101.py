A = int(input())
B = int(input())
C = int(input())

if A == B and B == C:
    print('Equilateral')
elif A + B + C == 180 and A == B or A == C or B == C:
    print('Isosceles')
elif A + B + C == 180 and A != B and B != C and A != C:
    print('Scalene')
elif A + B + C != 180:
    print('Error')