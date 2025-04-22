import  sys
import threading

def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        l = list(map(int, input().split()))
        r = list(map(int, input().split()))
        # Sum of "safe" picks that don't create any match:
        # for each color, you can pick up to max(li, ri) gloves
        S = 0
        extras = [0] * n
        for i in range(n):
            li = l[i]
            ri = r[i]
            if li >= ri:
                S += li
                extras[i] = ri
            else:
                S += ri
                extras[i] = li
        # We need the k-1 largest extras to compute the threshold
        extras.sort(reverse=True)
        # Sum of the largest (k-1) extras; if k=1, prefix sum is zero
        overflow_needed = sum(extras[:k-1])  # prefix_extra[k-1]
        # Minimal x satisfying x > S + overflow_needed
        # i.e., x = S + overflow_needed + 1
        x_min = S + overflow_needed + 1
        print(x_min)

if __name__ == "__main__":
    solve()