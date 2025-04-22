import sys

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        # Total '<' and '>' in s
        count_L = s.count('<')
        count_R = s.count('>')
        # RegionSmall for '<' picks, RegionLarge for '>' picks, RegionMid for a[1]
        small = list(range(1, count_L + 1))
        large = list(range(n - count_R + 1, n + 1))
        full_set = set(range(1, n + 1))
        mid_vals = full_set - set(small) - set(large)
        # There should be exactly one mid value
        mid = mid_vals.pop()

        # Build demands for a[2..n]: 'S' for small, 'L' for large
        demands = ['S' if ch == '<' else 'L' for ch in s]

        ans = [None] * n
        ans[0] = mid
        pos = 1  # Next position to fill in ans (0-based)

        i = 0
        while i < len(demands):
            tag = demands[i]
            j = i + 1
            while j < len(demands) and demands[j] == tag:
                j += 1
            length = j - i

            if tag == 'S':
                # Pick 'length' largest from small, assign in descending order
                block = small[-length:]
                small = small[:-length]
                block.sort(reverse=True)
                for x in block:
                    ans[pos] = x
                    pos += 1
            else:
                # tag == 'L'
                # Pick 'length' smallest from large, assign in ascending order
                block = large[:length]
                large = large[length:]
                block.sort()
                for x in block:
                    ans[pos] = x
                    pos += 1

            i = j

        print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()