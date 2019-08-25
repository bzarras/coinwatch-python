from coinwatch.jobs.FiveMin import fiveMinJob

def handler(event, context):
    try:
        fiveMinJob(2.5)
        return { "statusCode": 200 }
    except Exception as err:
        print(err)
        return { "statusCode": 500 }
