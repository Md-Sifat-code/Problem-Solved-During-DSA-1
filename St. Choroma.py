inputtaking = int(input())

for _ in range(inputtaking):
    numberoftestcase, x = map(int, input().split())

    p = list(range(numberoftestcase))

    if x < numberoftestcase:
        p[x], p[numberoftestcase - 1] = p[numberoftestcase - 1], p[x]

    print(*p)
