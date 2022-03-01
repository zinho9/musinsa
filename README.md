# for musinsa Pre-task

iam.py -> aws credential 을 기반으로 DAYS에 저장된 날짜보다 생성된지 오래된 IAM user을 찾는 Python script



Dockerfile -> iam.py를 빌드하는 dockerfile , ENV로 DAYS에 입력될 날짜 변경 가능


* 전제조건
aws_access_key, secret_access_key 를 알고있을것
aws configure 을 통한 access 정보 입력 한 후
~/.aws/credentials 에 access 정보가 default로 들어가있는 상황


local에서 dockerfile build시 명령어
docker run -v ~/.aws/:/root/.aws:ro iamtest
