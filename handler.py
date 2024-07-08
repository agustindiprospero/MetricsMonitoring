import json


def log(event, context):
    body = json.loads(event.get('body'))
    print(json.dumps(body))

    response = {
        "statusCode": 200,
        "body": json.dumps({"successful":"log register"})
    }

    return response