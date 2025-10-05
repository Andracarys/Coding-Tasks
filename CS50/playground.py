import sys
import requests

# Expects the user to specify as a command-line argument
# the number of Bitcoins: 𝑛, that they would like to buy.
# If that argument cannot be converted to a float,
# the program should exit via sys.exit with an error message.
# Queries the API for the CoinCap Bitcoin Price Index
# at rest.coincap.io/v3/assets/bitcoin?apiKey = YourApiKey.
# You should replace YourApiKey with the actual API key you obtained
# from your CoinCap account dashboard, which returns a JSON object,
# among whose nested keys is the current price of Bitcoin as a float.
# Be sure to catch any exceptions.
# Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places,
# using , as a thousands separator.

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    n = float(sys.argv[1])
    if n < 0:
        sys.exit("Command-line argument must be a positive number")
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=bd7d4b92fcd5e5b7ec00f8b461a3eb324ce133f3f34cbc350d8cdc39fdb27fe3",
        timeout=10)  # timeout added to avoid hanging indefinitely
    response.raise_for_status()
    bitcoin_data = response.json()


except requests.RequestException:
    sys.exit("Network error")

   # price = float(bitcoin_data["data"]["priceUsd"])
   # cost = n * price
    # print(f"${cost:,.4f}")
