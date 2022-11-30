#각 말의 수 입력
King, Queen, Rooks, Bishops, Nights, Pawns = 1, 1, 2, 2, 2, 8
#동혁이가 찾은 각 말의 수 입력
King_f, Queen_f, Rooks_f, Bishops_f, Nights_f, Pawns_f = map(int, input().split())
#필요한 말의 수 차이 출력
print(King-King_f, Queen-Queen_f, Rooks-Rooks_f, Bishops-Bishops_f, Nights-Nights_f, Pawns-Pawns_f)