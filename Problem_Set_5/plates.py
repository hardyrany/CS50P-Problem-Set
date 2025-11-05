def main():
    plate = input("Plate:\n")
    if is_valid(plate):
        print("Valid ")
    else:
        print("Invalid ")


def is_valid(string):
    if len(string) < 2 or len(string) > 6:
        return False
    if not string[0].isalpha() or not string[1].isalpha():
        return False
    if not all(char.isalnum() for char in string):
        return False

    flag = False
    for char in string:
        if char.isdigit():
            flag = True
        if char.isalpha() and flag:
            return False

    for char in string:
        if char.isdigit():
            return char != "0"

    return True


if __name__ == "__main__":
    main()
