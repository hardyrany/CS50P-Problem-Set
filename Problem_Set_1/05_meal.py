def main() -> None:
    input_time = input(
        "What time is it? Type: 7:00\n"
        "What time is it? Type: 7:30\n"
        "What time is it? Type: 12:42\n"
        "What time is it? Type: 18:32\n"
        "What time is it? Type: 11:11\n"
    )
    meal_time = convert(input_time)

    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")


def convert(time: str) -> float:
    hours_str, minutes_str = time.split(":")
    hours: float = float(hours_str.lstrip("0") or "0")
    minutes: float = float(minutes_str)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
