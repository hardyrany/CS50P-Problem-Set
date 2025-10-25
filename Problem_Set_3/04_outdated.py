months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError

        elif "," in date:
            month_str, day_year = date.split(" ", 1)
            day, year = day_year.replace(",", "").split(" ")

            if month_str not in months:
                raise ValueError

            month = months.index(month_str) + 1
            day = int(day)
            year = int(year)

            if day < 1 or day > 31:
                raise ValueError

        else:
            raise ValueError

        print(f"{year}-{month:02}-{day:02}")
        break

    except ValueError:
        continue
