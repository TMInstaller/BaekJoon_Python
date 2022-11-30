N, M = map(int, input().split())
print('N(세로) = ', N, 'M(가로) = ',M,'_line2')
#입력 후 2차원 배열에 저장
G_list = []
for i in range(N):
    G = input()
    if len(G) == M:
        print("올바른 입력_line 8")
        G_list[i].append(G)
    else:
        print("올바르지 않은 입력_line 10")
        break