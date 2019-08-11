import urllib.request as ur
import json
import boto3

def getLatestPrices():
    """
    Hardcoded to get coin data from CoinMarketCap.com
    
    Returns subset of that data containing only bitcoin, ethereum, and litecoin
    """
    
    conn = ur.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=20")
    raw_data = conn.read()
    coin_data = json.loads(raw_data.decode("utf8"))
    print("Successfully got price data from CoinMarketCap")

    interested_ids = { "bitcoin", "ethereum", "litecoin" }
    filtered_coins = [coin for coin in coin_data if coin["id"] in interested_ids]
    return filtered_coins

def getPreviousPrices():
    """
    Hardcoded to get coin data from S3
    """

    s3 = boto3.resource("s3")
    try:
        raw_data = s3.Object("coinwatch-data", "prices.json").get()
        prices = json.loads(raw_data["Body"].read().decode("utf8"))
        print("Successfully fetched price data from S3")
        return prices
    except Exception as err:
        print("Could not get previous prices from S3", err)
        return None

def persistPrices(prices):
    """
    Saves price data to S3
    """

    s3 = boto3.resource("s3")
    try:
        s3.Bucket("coinwatch-data").put_object(
            Key="prices.json",
            Body=json.dumps(prices)
        )
        print("Successfully uploaded price data to S3")
    except Exception as err:
        print("Failed to upload prices", err)
