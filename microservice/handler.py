# must be called as we're using zipped requirements
try:
    import unzip_requirements
except ImportError:
    pass

try:
    import json
    import os
    from pynamodb.models import Model
    from pynamodb.attributes import *
except Exception as e:
    print("Some Modules are Missing :{} ".format(e))

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_VALUE")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY_VALUE")
region = os.getenv("AWS_REGION_VALUE")
TABLE_NAME = os.getenv("TABLE_NAME")


class UserModel(Model):
    class Meta:
        region = region
        table_name = TABLE_NAME
        aws_access_key_id = AWS_ACCESS_KEY
        aws_secret_access_key = AWS_SECRET_KEY

    email = UnicodeAttribute(hash_key=True)
    userId = UnicodeAttribute(range_key=True)
    region = UnicodeAttribute(null=True)
    first_name = UnicodeAttribute(null=True)
    last_name = UnicodeAttribute(null=True)
    company = ListAttribute()


def get_record(event, context):
    print(event)

    body = event.get("body")
    serialized_payload = json.loads(body)
    email = serialized_payload.get("email", None)
    if email is None:
        return {"statusCode": 200, "body": json.dumps(" Cannot find item ")}
    else:
        data = {}
        for user in UserModel.query(email):
            data = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "company": user.company,
                "region": user.region,
            }
        return {"statusCode": 200, "body": json.dumps(data)}


