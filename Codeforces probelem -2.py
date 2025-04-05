import math


def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        size = int(input())

        numbers = list(map(int, input().split()))

        min_value = min(numbers)

        min_count = numbers.count(min_value)

        divisor_count = 0
        quotients = []
        is_min = []

        for num in numbers:
            if num % min_value == 0:
                quotients.append(num // min_value)
                is_min.append(1 if num == min_value else 0)
                divisor_count += 1

        overall_gcd = quotients[0]
        for quotient in quotients[1:]:
            overall_gcd = compute_gcd(overall_gcd, quotient)

        if overall_gcd != 1:
            print("No")
            continue

        if divisor_count < 2:
            print("No")
            continue

        prefix_gcd = [0] * divisor_count
        suffix_gcd = [0] * divisor_count

        prefix_gcd[0] = quotients[0]
        for i in range(1, divisor_count):
            prefix_gcd[i] = compute_gcd(prefix_gcd[i - 1], quotients[i])

        suffix_gcd[divisor_count - 1] = quotients[divisor_count - 1]
        for i in range(divisor_count - 2, -1, -1):
            suffix_gcd[i] = compute_gcd(suffix_gcd[i + 1], quotients[i])

        is_possible = False
        for i in range(divisor_count):
            if is_min[i]:
                gcd_without_current = 0
                if i > 0:
                    gcd_without_current = prefix_gcd[i - 1]
                if i < divisor_count - 1:
                    if gcd_without_current == 0:
                        gcd_without_current = suffix_gcd[i + 1]
                    else:
                        gcd_without_current = compute_gcd(gcd_without_current, suffix_gcd[i + 1])

                if gcd_without_current == 1:
                    is_possible = True
                    break

        if is_possible:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
