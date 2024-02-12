N = int(input())
score_list = list(map(int, input().split()))

_max = max(score_list)

new_score_list = []

for score in score_list:
    new_score_list.append(score/_max * 100)

print(sum(new_score_list)/N)