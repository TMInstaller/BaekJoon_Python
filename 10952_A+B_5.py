while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0:
        break
    result = sum(a)
    print(result)