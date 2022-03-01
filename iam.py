import sys
import boto3
import os
from datetime import datetime, timedelta, timezone

# local에서 python3 로 실행시 사용, input으로 생성 후 몇일이 지났는지 기준 입력
# DAYS = int(input("The days after creation : "))
DAYS = int(os.environ['DAYS'])

iamclient = boto3.client('iam')
stsclient = boto3.client('sts')

identity = stsclient.get_caller_identity()
account = identity['Account']
ok = False

count = 0
today = datetime.now(timezone.utc)

for user in iamclient.list_users()['Users']:
    arn = user['Arn']
    username = user['UserName']

    keys = iamclient.list_access_keys(UserName=username)

    for key in keys['AccessKeyMetadata']:
        accessid = key['AccessKeyId']
        created = key['CreateDate']
        created_date = today - created

        if created + timedelta(days=DAYS) < today:
            count += 1

            if not ok:
                ok = True
                print(f'Username, Access Key, CreationTime, Days_after_creation')

            print(f'{username}, {accessid}, {created}, {created_date.days}days', end = '\n')

sys.exit(count)