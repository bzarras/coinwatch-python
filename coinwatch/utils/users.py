import boto3
import json
from coinwatch.types.User import User

def getSubscribedUsers(coins):
    """
    raw data looks like:
    {
        "BTC": [{
            "email": "",
            "phrase": ""
        }],
        "ETH": [{
            "email": "",
            "phrase: ""
        }]
    }
    """
    s3 = boto3.resource("s3")
    try:
        raw_data = s3.Object("coinwatch-data", "users.json").get()
        raw_users = json.loads(raw_data["Body"].read().decode("utf8"))
        print("Successfully fetched user data from S3")
        
        users = []
        user_dict = {}
        for coin in coins:
            user_list = raw_users.get(coin.symbol, [])
            for raw_user in user_list:
                user_email = raw_user["email"]
                user = user_dict.get(user_email, None)
                if not user:
                    user = User(user_email, raw_user["phrase"])
                    user_dict[user_email] = user
                user.subscribeToCoin(coin)
        for key in user_dict.keys():
            users.append(user_dict[key])
        return users
    except Exception as err:
        print("Could not get user data from S3", err)
        return None
