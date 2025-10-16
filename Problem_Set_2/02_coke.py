def main():
    change_calc()


def change_calc():
    amount_due = 50
    accepted_coins = [5, 10, 25]
    coins_added = 0

    while True:
        print(f"Amount Due: {amount_due}")
        print(f"Acceted Coins: {accepted_coins}")
        insert_coin: int = int(input("Insert Coin: "))
        print(f"Coins Added: {coins_added + insert_coin}")
        if insert_coin in accepted_coins:
            amount_due -= insert_coin
            coins_added += insert_coin
        if amount_due <= 0:
            break
        else:
            print("Coin not accepted")

    change_owed = abs(coins_added - 50)
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
