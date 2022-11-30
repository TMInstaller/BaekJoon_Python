#테스트 케이스 개수 C
C = int(input())
C_list = []

for i in range(C):
    #평균 이상의 학생을 담을 변수 count 초기화
    count = 0
    #C_list에 학생 수와 점수 입력
    C_list = list(map(int, input().split()))
    #print(C_list,'_line 10_ C_list')
    N = C_list[0]
    #배열의 수 전부 합산, 학생 수 만큼 뺀 후 평균 구하기
    C_sum = sum(C_list) - N
    C_ave = C_sum/N
    #print(C_ave,'_line 15_ C_ave')
    #C_list에 들어간 수 중에 C_ave보다 큰 수가 발견되면 count ++
    for i in range(len(C_list)):
        if i != 0:
            if C_list[i] > C_ave:
                count+=1
    #print(count,'_line 21_ count')
    #C_p라는 상위 퍼센트를 담는 변수를 지정 후 f-string을 이용해 소숫점 조절
    C_p = count/N*100
    print(f"{C_p:.3f}%")