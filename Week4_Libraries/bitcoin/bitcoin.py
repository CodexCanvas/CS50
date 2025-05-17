import requests
import json
import sys

def get_btc_price(api_key):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&CMC_PRO_API_KEY={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for item in data['data']:
            if item['symbol'] == 'BTC':
                return item['quote']['USD']['price']
        return None  # Bitcoin not found
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error parsing JSON response: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        num_btc = float(sys.argv[1])
        if num_btc <= 0:
            print("Number of bitcoins must be positive.")
            sys.exit(1)
    except ValueError:
        print("Invalid input: Number of bitcoins must be a number.")
        sys.exit(1)

    api_key = 'b036a635-2bf2-44c1-8b19-33790d68036c'  # Replace with your actual API key
    price = get_btc_price(api_key)

    if price is not None:
        total_cost = num_btc * price
        print(f"The price of {num_btc:.2f} BTC is: ${total_cost:.2f}")
    else:
        print("Could not retrieve Bitcoin price.")