import json
import cv2
import io
import numpy as np
import base64
def meow(event, context):


    # nparr = np.fromstring(base64.b64decode(event.body), np.uint8)
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # h, w = img.shape[:2]
    # # #To shrink an image, it will generally look best with cv::INTER_AREA interpolation, whereas to enlarge an image, it will generally look best with cv::INTER_CUBIC (slow) or cv::INTER_LINEAR (faster but still looks OK).
    # img = cv2.resize(img, (3*w, 3*h), interpolation = cv2.INTER_CUBIC)   
    # kernel_sharpening = np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    # img = cv2.filter2D(img, -1, kernel_sharpening)
    # retval, buffer = cv2.imencode('.jpg', img)
    # word = (base64.b64encode(buffer))
    # body = (base64.b64decode(word))

    print(event)
    print("Time remaining (MScvy):", context.get_remaining_time_in_millis())
    return {
        "statusCode": 200,
        "body": json.dumps("sdfsf")
    }


