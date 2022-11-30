#수 N(10)개 입력받기
N = 10
#비어있는 list 선언
N_list = []
#10개의 수를 입력받으며 42로 나눈 나머지를 배열에 넣기
for i in range(N):
    N_list.append(int(input()))
    N_list[i] = N_list[i]%42

#set함수 : 순서상관없이 중복값만 제거하는 함수
result = list(set(N_list))
#제거된 배열의 길이 = 서로 다른 나머지의 수
print(len(result))