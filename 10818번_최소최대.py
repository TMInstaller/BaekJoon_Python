#정수 N 입력
N = int(input())
#정수 N개 만큼 배열로 입력
N_list = list(map(int, input().split()))
#가장 작은 수와 큰 수를 공백 구분 출력
print(min(N_list), max(N_list))