import json
import cv2
import io
import numpy as np
import base64
import pika
def meow(event, context):


    nparr = np.fromstring(base64.b64decode(event['body']), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    h, w = img.shape[:2]
    # #To shrink an image, it will generally look best with cv::INTER_AREA interpolation, whereas to enlarge an image, it will generally look best with cv::INTER_CUBIC (slow) or cv::INTER_LINEAR (faster but still looks OK).
    img = cv2.resize(img, (3*w, 3*h), interpolation = cv2.INTER_CUBIC)   
    kernel_sharpening = np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel_sharpening)

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    print("Found {0} faces!".format(len(faces)))

    retval, buffer = cv2.imencode('.jpg', img)
    word = (base64.b64encode(buffer))
    body = (base64.b64decode(word))

    credentials = pika.PlainCredentials('kat', 'meow')
    parameters = pika.ConnectionParameters('128.125.225.215',5672,'/',credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_publish(exchange='kex',routing_key='kq',body=body)
    connection.close()
    print("Time remaining (MScvy):", context.get_remaining_time_in_millis())
#    return body
    return {
        "statusCode": 200,
        "body": "sssf"
    }



