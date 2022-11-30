#테스트 케이스 개수 N
N = int(input())
N_list = []
#N개의 테스트 케이스 출력
for i in range(N):
    #OX퀴즈의 점수 초기화
    score = 0
    #연속되는 문제의 수를 나타내는 count 초기화
    count = 0

    #N_list의 배열에 무작위 OX문자열 입력
    N_list.append(input())
    #print(N_list, '_line 7')

    #N_input에 입력받은 문자열을 각각 분리
    N_input = list(N_list[i])
    #print(N_input, '_line 9')

    #i번째 테스트 케이스에 N_input에 나눠놓은 OX문자열 분석 로직
    for i in range(len(N_input)):
        #O일 경우엔 연속성(count) 1씩 증가하며 score에 합산
        if N_input[i] == 'O':
            count+=1
            score+=count
            #print(i,'번째 점수: ',score,'점')
        #O가 아닐 경우엔 연속성 초기화, 점수 미 증가
        else:
            count = 0
    #i번째 테스트 케이스 점수 출력
    print(score)