from jobs.FiveMin import fiveMinJob

def handler(event, context):
    fiveMinJob()
    return { "statusCode": 200 }
