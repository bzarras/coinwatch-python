class Coin:
    def __init__(self, raw_data):
        self.id = raw_data["id"]
        self.name = raw_data["name"]
        self.symbol = raw_data["symbol"]
        self.price_usd = float(raw_data["price_usd"])
        self.percent_change_1h = float(raw_data["percent_change_1h"])
        self.percent_change_24h = float(raw_data["percent_change_24h"])
        self.percent_change_5m = None # to be overridden later by clients

    def dump(self):
        print(self.__dict__)
    
    def asDict(self):
        return self.__dict__

    def renderHTMLChangeString(self):
        color = "green" if self.percent_change_5m >= 0 else "red"
        return '<p style="color:{color};">{symbol}: ${price}, change: {change} %</p>'.format(
            color=color,
            symbol=self.symbol,
            price=round(self.price_usd, 2),
            change=round(self.percent_change_5m, 2)
        )
