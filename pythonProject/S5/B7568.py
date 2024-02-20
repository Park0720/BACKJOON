N = int(input())

person_list = [list(map(int, input().split())) for _ in range(N)]

sort_rank_list = [0] * N
rank_list = [0] * N
max_kg, max_cm = 0, 0

for person in person_list:
    if person[0] > max_kg and person[1] > max_cm:
        max_kg, max_cm = person[0], person[1]

sort_person_list = sorted(person_list, reverse=True)

count = 1
same_count = 0

for i in range(N):
    if sort_person_list[i][0] == max_kg and sort_person_list[i][1] == max_cm:
        sort_rank_list[i] = count

    elif sort_person_list[i][0] > max_kg and sort_person_list[i][1] < max_cm:
        same_count += 1
        sort_rank_list[i] = count

    elif sort_person_list[i][0] < max_kg and sort_person_list[i][1] > max_cm:
        same_count += 1
        sort_rank_list[i] = count

    elif sort_person_list[i][0] < max_kg and sort_person_list[i][1] < max_cm:
        max_kg, max_cm = sort_person_list[i][0], sort_person_list[i][1]
        count += 1
        sort_rank_list[i] = count + same_count
        same_count = 0

for i in range(N):
    for j in range(N):
        if sort_person_list[i] == person_list[j]:
            rank_list[j] = sort_rank_list[i]

print(sort_person_list)
print(*sort_rank_list)
print(*rank_list)