import boto3
import os
from pathlib import Path
from botocore.exceptions import NoCredentialsError

access_file = open(str(Path.home()) + "/.passwd-s3fs", "r")
keys = access_file.read().split(':')
ACCESS_KEY = keys[0]
SECRET_KEY = (keys[1])[:len(keys[1])-1]

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY, 
                      endpoint_url="https://s3-us-east-2.amazonaws.com")
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


for file in os.listdir('.'):
    if file.endswith('.tar.gz'):
        print('Uploading ' + file + ' to S3 bucket...')
        upload_to_aws(file, 'mcworldbackups', file)
        print('Success.')
        os.remove(file)
    else:
        print('File ' + file + ' does not end with tar.gz')
