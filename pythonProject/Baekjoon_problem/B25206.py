grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0,
}
sum_score = 0
sum_grade_score = 0
for _ in range(20):
    class_name, score, my_grade = map(str, input().split())
    if my_grade != 'P':
        sum_score += float(score)
        sum_grade_score += float(score) * grade.get(my_grade)

print(sum_grade_score / sum_score)