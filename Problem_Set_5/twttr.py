def main():
    user_input = input("Type:\n")

    print(shorten(user_input))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = ""
    for char in word:
        if char.casefold() not in vowels:
            no_vowels += char
    return no_vowels


if __name__ == "__main__":
    main()
