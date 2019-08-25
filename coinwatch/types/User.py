import urllib

class User():
    def __init__(self, email, phrase):
        self.email = email
        self.phrase = phrase
        self._subscribed_coins = []

    def subscribeToCoin(self, coin):
        self._subscribed_coins.append(coin)

    def getSubscribedCoins(self):
        return self._subscribed_coins

    def notify(self, email_client):
        subject = "Coinwatch price alert"
        changes = "".join([coin.renderHTMLChangeString() for coin in self._subscribed_coins])
        body = '{changes}<p style="font-size: 10px;"><a href="https://www.coinwatch.fyi/unsubscribe?email={email}&phrase={phrase}">unsubscribe</a></p>'.format(
            changes=changes,
            email=urllib.parse.quote(self.email, safe=""),
            phrase=self.phrase
        )
        email_client.send(
            recipient=self.email,
            subject=subject,
            body=body
        )
