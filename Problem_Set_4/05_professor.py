import random


def main():
    level = get_level()
    score = calc_result(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    start, stop = ranges[level]
    return random.randint(start, stop)


def calc_result(level):
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        attempts = 3
        while attempts > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    attempts -= 1
                    print("EEE")
            except ValueError:
                attempts -= 1
                print("EEE")

        if attempts == 0:
            print(f"{x} + {y} = {correct}")

    return score


if __name__ == "__main__":
    main()
