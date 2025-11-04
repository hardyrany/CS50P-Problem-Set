import inflect


p = inflect.engine()


def main():
    sing_adieu()


def sing_adieu():
    names = []
    try:
        while True:
            name = input("Type: Lies1\n")
            names.append(name)
    except EOFError:
        print("\nAdieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
