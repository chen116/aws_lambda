import json

def meow(event, context):
    print("Time remaining (MScvy):", context.get_remaining_time_in_millis())
    return {
        "statusCode": 200,
        "body": json.dumps('dHello from Lambdasssscv!')
    }

