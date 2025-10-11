import boto3
import os
import json

bucket = 'sagemaker-us-east-2-344400919253'

def put(path, body):
    s3 = boto3.client(service_name="s3", aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                      aws_secret_access_key=os.environ['AWS_SECRET_KEY'], region_name='us-east-2')
    s = s3.put_object(Body=json.dumps(body), Bucket=bucket, Key=path)


def get(key):
    get_s3 = boto3.client(service_name="s3", aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY'], region_name='us-east-2')
    obj = get_s3.get_object(Bucket=bucket, Key=key)
    return json.loads(obj['Body'].read())


