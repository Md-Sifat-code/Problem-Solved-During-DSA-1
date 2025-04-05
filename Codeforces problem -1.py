def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        if n % 2 == 0:
            print(-1)
        else:
            result = [n, 1]
            result.extend(range(2, n))
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
