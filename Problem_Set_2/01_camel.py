def main():
    camelCase: str = input("camelCase:\n")
    print(camel_to_snake(camelCase))


def camel_to_snake(camelCase: str):
    snake_case = ""
    for char in range(len(camelCase)):
        if camelCase[char].isupper():
            snake_case = snake_case + "_" + camelCase[char].lower()
        else:
            snake_case += camelCase[char]

    return snake_case


if __name__ == "__main__":
    main()
