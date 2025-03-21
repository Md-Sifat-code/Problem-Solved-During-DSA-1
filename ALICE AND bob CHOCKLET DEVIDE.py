total_test_case = int(input())
for _ in range(total_test_case):
    A,B = map(int, input().split())
    if (A+B) %2 ==0:
        print("YES")
    else:
        print("NO")
