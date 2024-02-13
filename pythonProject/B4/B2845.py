L, P = map(int, input().split())
people_list = list(map(int, input().split()))

answer = L * P
wrong_list = []

for person in people_list:
    wrong_list.append(person - answer)

print(*wrong_list)