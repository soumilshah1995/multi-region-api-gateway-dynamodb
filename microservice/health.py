import json


def check(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(' OK ')
    }
