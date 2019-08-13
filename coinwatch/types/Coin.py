class Coin:
    def __init__(self, raw_data):
        self.id = raw_data["id"]
        self.name = raw_data["name"]
        self.symbol = raw_data["symbol"]
        self.price_usd = float(raw_data["price_usd"])
        self.percent_change_1h = float(raw_data["percent_change_1h"])
        self.percent_change_24h = float(raw_data["percent_change_24h"])
