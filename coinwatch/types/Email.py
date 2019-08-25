import boto3

class EmailClient():

    def __init__(self):
        self.ses_client = boto3.client("ses")

    def send(self, recipient, subject, body):
        try:
            self.ses_client.send_email(
                Source='"Coinwatch" <donotreply@coinwatch.fyi>',
                Destination={
                    "ToAddresses": [recipient]
                },
                Message={
                    "Subject": {
                        "Data": subject,
                        "Charset": "utf-8"
                    },
                    "Body": {
                        "Html": {
                            "Data": body,
                            "Charset": "utf-8"
                        }
                    }
                }
            )
        except Exception as err:
            print("Failed to send email with SES", err)
