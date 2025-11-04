import sys
import requests


def main():
    n = get_bitcoin_amount()
    price = get_bitcoin_price()
    display_results(price, n)


def get_bitcoin_amount():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price():
    url = "https://rest.coincap.io/v2/assets/bitcoin"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching data from CoinCap API")

    data = response.json()
    return float(data["data"]["priceUsd"])


def display_results(price, n):
    print(f"Current Bitcoin price: ${price:,.4f}")
    total = price * n
    print(f"Total cost for {n} Bitcoin(s): ${total:,.4f}")


if __name__ == "__main__":
    main()
