#시험을 본 과목의 개수 N
N = int(input())

N_list = []
#시험을 본 실제 성적
N_list = list(map(int, input().split()))

#조작을 위해 필요한 가장 잘 본 시험점수 M
M = max(N_list)
ev = 0
#주의사항: Max값은 가만 두어야 한다는 편견을 버려야 함
for i in range(N):
    ev += N_list[i]/M*100

print(ev/N)