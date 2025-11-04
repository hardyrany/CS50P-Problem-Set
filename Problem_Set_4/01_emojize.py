import emoji


def main():
    emojize()


def emojize():
    user_input = input(
        "Type :1st_place_medal:\n"
        "Type :money_bag:\n"
        "Type :smile_cat:\n"
    )
    print(emoji.emojize(user_input, language="alias"))


if __name__ == "__main__":
    main()
