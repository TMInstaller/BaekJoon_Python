# 1. 문자열 S 입력
S = input()
# 2. 알파벳 목록 alphabets 입력
alphabets = 'abcdefghijklmnopqrstuvwxyz'
# 3. 각각의 alphabets 요소들에 대해 위치 확인하는 반복문
for i in alphabets:
    # 3.1 안에 들어있으면 find함수의 값 출력
    #     find = 찾은 목표의 첫 번째 위치를 가져온다
    if i in S:
        print(S.find(i),end=' ')
    # 3.2 예외처리 -1출력
    else:
        print(-1,end=' ')