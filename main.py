import problems as prob


def main():
    k = int(input())
    x_min, y_min, x_max, y_max = list(map(int, input().split())) * 2

    for _ in range(k - 1):
        x, y = list(map(int, input().split()))

        if x < x_min:
            x_min = x
        elif x > x_max:
            x_max = x

        if y < y_min:
            y_min = y
        elif y > y_max:
            y_max = y

    print(f"{x_min} {y_min} {x_max} {y_max}")


if __name__ == "__main__":
    main()
