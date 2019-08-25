from coinwatch.jobs.FiveMin import fiveMinJob
import os

def handler(event, context):
    try:
        percent_threshold = os.environ.get("PERCENT_THRESHOLD", 2.5)
        fiveMinJob(percent_threshold)
        return { "statusCode": 200 }
    except Exception as err:
        print(err)
        return { "statusCode": 500 }
