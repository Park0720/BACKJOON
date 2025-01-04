N = int(input())
person_list = [list(map(int, input().split())) for _ in range(N)]

rank_list = [1] * N  # 모든 사람의 초기 등수는 1로 설정

# 모든 사람을 서로 비교하여 등수 계산
for i in range(N):
    for j in range(N):
        if i != j:  # 자기 자신과 비교하지 않음
            if person_list[i][0] < person_list[j][0] and person_list[i][1] < person_list[j][1]:
                rank_list[i] += 1  # 자신보다 덩치가 큰 사람이 있으면 등수 증가

print(*rank_list)
