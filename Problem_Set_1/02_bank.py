"""Process user greeting and return corresponding dollar value"""


def main():
    """Process user greeting and return corresponding dollar value"""
    user_input = input(
        "Greeting: Hello\n"
        "Greeting: Hello, Newman\n"
        "Greeting: How you doing?\n"
        "Greeting: What's happening?\n"
    )
    greeting_results = greeting(user_input.lower().strip())
    print(greeting_results)


def greeting(g):
    """Returns dollar values based on greeting"""
    if g.startswith("hello"):
        return "$0"
    elif g == "hello, newman":
        return "$0"
    elif g == "how you doing?":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
