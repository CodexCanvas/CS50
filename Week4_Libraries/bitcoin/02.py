from coinmarketcapapi import CoinMarketCapAPI

api_key = 'b036a635-2bf2-44c1-8b19-33790d68036c'  # Replace with your actual API key
cmc = CoinMarketCapAPI(api_key)

try:
    data = cmc.cryptocurrency_info(symbol='BTC')
    for item in data.data:
        if item['symbol'] == 'BTC':
            price = item['quote']['USD']['price']
            print(f"Bitcoin price (USD): {price}")
            break
    else:
        print("Bitcoin data not found.")

except Exception as e:
    print(f"An error occurred: {e}")