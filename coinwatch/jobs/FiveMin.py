import urllib.request as ur
import json
from coinwatch.utils.prices import getLatestPrices, getPreviousPrices, persistPrices

def fiveMinJob():
    """
    Get new prices
    Get previous prices
    Persist new prices as previous prices
    Compute difference and see if change > threshold
    For each coin that changed enough
        Get interested recipients
        Add recipient to dictionary of recipient name: coins
    For each recpient in dictionary
        Send email with price change info
    Done
    """
    print("Running five minute job!")
    new_coin_prices = getLatestPrices()
    old_coin_prices = getPreviousPrices()

    if not old_coin_prices:
        persistPrices(new_coin_prices)
