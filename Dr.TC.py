t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    count1 = s.count('1')

    result = (n - count1) + count1 * (n - 1)

    print(result)
