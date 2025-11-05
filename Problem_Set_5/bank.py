def main():
    user_input = input("Greeting:\n")
    greeting_results = value(user_input)
    print(greeting_results)


def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
