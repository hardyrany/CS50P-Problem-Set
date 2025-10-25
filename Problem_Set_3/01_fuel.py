def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")

            x = int(x)
            y = int(y)

            if y == 0 or x > y or x < 0 or y < 0:
                raise ValueError

            fuel = round((x / y) * 100)

        except (ValueError, ZeroDivisionError):
            continue
        else:
            break

    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


if __name__ == "__main__":
    main()
