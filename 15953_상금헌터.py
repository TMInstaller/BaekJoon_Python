# 2017년 코드 페스티벌 등수에 따른 상금
# 순위권 외적인 부분을 표현하기 위해 리스트의 0번째 부분은
# 상금을 0으로 두었다
K_2017 = [0, 500]
for i in range(2):
    K_2017.append(300)
for i in range(3):
    K_2017.append(200)
for i in range(4):
    K_2017.append(50)
for i in range(5):
    K_2017.append(30)
for i in range(6):
    K_2017.append(10)
# 2017년 코드 페스티벌 등수에 따른 상금
# 마찬가지로 리스트의 0번째 부분은
# 상금을 0으로 두었다
K_2018 = [0, 512]
for i in range(2):
    K_2018.append(256)
for i in range(4):
    K_2018.append(128)
for i in range(8):
    K_2018.append(64)
for i in range(16):
    K_2018.append(32)
# 가정한 횟수 T
T = int(input())
# T회동안의 로직
for i in range(T):
    # 1회차 등수, 2회차 등수 입력
    a, b = map(int, input().split())
    # 순위권 밖일 경우 상금을 0으로 두는 작업 진행
    if a > 21:
        a = 0
    if b > 31:
        b = 0

    # 리스트의 0번째 값이 0이므로 a, b는 그대로 들어가면된다
    rew = (K_2017[a] + K_2018[b])*10000
    # 결과 출력
    print(rew)