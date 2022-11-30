# 주어진 정수 N 입력
N = int(input())
# 정수를 담을 list생성
essence = list(map(int, input().split()))
# 찾으려는 정수 v 입력
v = int(input())
# list에서 v를 count한 값을 출력
print(essence.count(v))
