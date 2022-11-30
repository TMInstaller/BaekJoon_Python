# 1. 제출 한 과제 목록을 불러올 list 생성
SWD = []
# 2. 전체 학생 번호 list 생성
swd = []
# 3. 제출한 학생 목록 list에 넣기
for i in range(28):
    SWD.append(int(input()))
# 4. 전체 학생 목록 list에 넣기
for i in range(30):
    swd.append(i+1)

# 5. 전체 학생 목록과 제출한 학생 목록의 차집합 구하기
swd_p = list(set(swd) - set(SWD))
# 6. 차집합 작은 수 부터 정렬
swd_p.sort()

# 7. 안 해온 학생 앞 두 번호 출력
print(swd_p[0])
print(swd_p[1])