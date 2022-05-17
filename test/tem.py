import os
import boto3
import json
from faker import Faker
import random
import pynamodb.attributes as at
import datetime
from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import *


AWS_ACCESS_KEY = "AKIA4TYY74BHW7EUHY7Q"
AWS_SECRET_KEY = "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"
region = "us-east-1"


class UserModel(Model):
    class Meta:
        region = region
        table_name = "users"
        aws_access_key_id = AWS_ACCESS_KEY
        aws_secret_access_key = AWS_SECRET_KEY

    email = UnicodeAttribute(hash_key=True)
    userId = UnicodeAttribute(range_key=True)
    region = UnicodeAttribute(null=True)
    first_name = UnicodeAttribute(null=True)
    last_name = UnicodeAttribute(null=True)
    company = ListAttribute()


for user in UserModel.query("qhanson@example.com"):
    _data = {
        "first_name":user.first_name,
        "last_name":user.last_name,
        "company":user.company
    }
    print(_data)
