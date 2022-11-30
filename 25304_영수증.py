#총 구매금액  X입력
X = int(input())
#영수증에 적힌 구매물건 종류 수 N 입력
N = int(input())
#구매물건 총액 저장 변수 X0 선언
X0 = 0
#N개 만큼 입력하는 반복문 실행
i = 0
while i < N:
    #새로운 배열에 집어넣기
    a, b = map(int, input().split())
    #배열 a0, b0에 a, b추가
    X0 = X0 + a*b
    i+=1
#결과 출력
if X == X0:
    print('Yes')
else:
    print('No')