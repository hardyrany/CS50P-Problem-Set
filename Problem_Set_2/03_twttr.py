def main():
    user_input = input(
        "Type: Twitter\n"
        "Type: What's your name?\n"
        "Type: CS50\n"
    )

    print(vowels(user_input))


def vowels(str_vowel):
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = ""
    for char in str_vowel:
        if char.casefold() not in vowels:
            no_vowels += char
    return no_vowels


if __name__ == "__main__":
    main()
