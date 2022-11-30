#9개의 정수 입력
N = 9
#9개의 수를 입력받을 비어있는 배열 선언
N_list = []
#반복문을 통해 N개의 -정수-입력
for i in range(N):
    #int형 입력이 아닐 시 최대값 판별 불가능
    N_list.append(int(input()))
result = max(N_list)
print(result)
#첫 번째 자리는 0으로 출력되므로 +1하기
print(N_list.index(result)+1)