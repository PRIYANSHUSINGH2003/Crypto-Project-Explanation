import requests
import pandas as pd

def fetch_crypto_data(crypto_pair, start_date):
    # Map the cryptocurrency to the CoinGecko ID
    coin_id = crypto_pair.split('/')[0].lower()  # e.g., 'bitcoin' for BTC
    vs_currency = crypto_pair.split('/')[1].lower()  # e.g., 'usd'

    # CoinGecko API URL
    base_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
    params = {
        'vs_currency': vs_currency,  # Currency to compare against
        'from': pd.Timestamp(start_date).timestamp(),  # Start date in UNIX timestamp
        'to': pd.Timestamp.now().timestamp()  # Current date in UNIX timestamp
    }

    print(f"Fetching data from: {base_url} with params: {params}")  # Debugging log

    response = requests.get(base_url, params=params)
    data = response.json()

    # Check for errors in response
    if response.status_code != 200 or 'prices' not in data:
        raise Exception("Error fetching data: {}".format(data.get('error', 'Unknown error')))

    # Convert the response into a DataFrame
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['Date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['Open'] = df['price'].shift(1)  # Assume the previous price as Open
    df['Close'] = df['price']  # Current price as Close
    df['High'] = df['price'].rolling(window=1).max()  # Initialize High
    df['Low'] = df['price'].rolling(window=1).min()  # Initialize Low

    # Set Open, High, Low for the first record correctly
    df.loc[0, 'Open'] = df.loc[0, 'price']
    df['High'] = df['High'].ffill()  # Forward fill to maintain the highest price seen
    df['Low'] = df['Low'].ffill()  # Forward fill to maintain the lowest price seen

    return df[['Date', 'Open', 'High', 'Low', 'Close']]
