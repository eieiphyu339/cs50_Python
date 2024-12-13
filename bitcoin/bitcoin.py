import requests, sys

def main():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    if len(sys.argv) != 2:
         print("Usage: python script.py <number_of_coins>")
         sys.exit(1)
    try:
        coins = float(sys.argv[1])
        if coins<1:
             raise ValueError("Number of coins must be at least 1.")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # updated_time = data["time"]["updated"]
        usd_rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        amount = usd_rate * coins
        print(f"${amount:,.4f}")

    except ValueError:
        print("Please provide a valid integer/decimal number of coins.")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()
