import json


def log(event, context):
    body = json.loads(event.get('body'))
    print(body)

    response = {
        "statusCode": 200,
        "message": "log register"
    }

    return response