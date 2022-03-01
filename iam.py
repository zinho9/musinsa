import sys
import boto3
import os
from datetime import datetime, timedelta, timezone

# DAYS = int(input("The days after creation : "))       
# local에 저장된 ./aws/credentials 로 사용할때 , days input으로 받아서 사용
DAYS = int(os.environ['DAYS'])

iam = boto3.client('iam')
sts = boto3.client('sts')

identity = sts.get_caller_identity()
account = identity['Account']
header_printed = False

count = 0
today = datetime.now(timezone.utc)

for user in iam.list_users()['Users']:
    arn = user['Arn']
    username = user['UserName']

    keys = iam.list_access_keys(UserName=username)

    for key in keys['AccessKeyMetadata']:
        accessid = key['AccessKeyId']
        created = key['CreateDate']
        created_date = today - created

        if created + timedelta(days=DAYS) < today:
            count += 1

            if not header_printed:
                header_printed = True
                print(f'Username, Access Key, CreationTime, Days_after_creation')

            print(f'{username}, {accessid}, {created}, {created_date.days}days', end = '\n')

sys.exit(count)
