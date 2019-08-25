import urllib.request as ur
import json
from coinwatch.utils.prices import getLatestPrices, getPreviousPrices, persistPrices
from coinwatch.utils.users import getSubscribedUsers
from coinwatch.types.Email import EmailClient

def fiveMinJob(threshold_percent):
    print("Running five minute job!")

    new_coin_prices = getLatestPrices()
    old_coin_prices = getPreviousPrices()
    persistPrices(new_coin_prices)
    
    coins_above_threshold = filterCoinsAboveThreshold(new_coin_prices, old_coin_prices, threshold_percent)

    # Exit early if there is nothing to do
    if len(coins_above_threshold) == 0:
        print("Price changes are not significant enough. Doing nothing.")
        return
    
    print("Sending email to users about {coins}".format(
        coins=", ".join([coin.symbol for coin in coins_above_threshold])
    ))
    
    email_client = EmailClient()
    users = getSubscribedUsers(coins_above_threshold)
    
    for user in users:
        user.notify(email_client)

def filterCoinsAboveThreshold(new_coins, old_coins, threshold):
    coins_above_threshold = []
    for new_coin in new_coins:
        old_coin = [c for c in old_coins if c.id == new_coin.id][0]
        percent_diff = (new_coin.price_usd - old_coin.price_usd) / old_coin.price_usd
        if abs(percent_diff) >= threshold:
            new_coin.percent_change_5m = percent_diff
            coins_above_threshold.append(new_coin)
    return coins_above_threshold
