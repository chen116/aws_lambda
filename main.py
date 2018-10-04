import json
import cv2
import io
import numpy
import base64
def meow(event, context):
    print("Time remaining (MScvy):", context.get_remaining_time_in_millis())
    return {
        "statusCode": 200,
        "body": json.dumps('dHello from Lambdasssscv2 nowayyyy!')
    }

