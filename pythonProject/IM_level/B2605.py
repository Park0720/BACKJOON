T = int(input())
student_num_list = list(map(int, input().split()))

student_line_list = []
for i in range(T):
    student_line_list.insert(i-student_num_list[i], i + 1)

print(*student_line_list)