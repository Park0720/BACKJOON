L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

a_val = 0
b_val = 0
if A % C == 0:
    a_val += A // C
else:
    a_val += A // C + 1

if B % D == 0:
    b_val += B // D
else:
    b_val += B // D + 1

if a_val > b_val:
    print(L - a_val)
else:
    print(L - b_val)
