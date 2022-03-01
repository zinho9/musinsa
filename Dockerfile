FROM python
WORKDIR /Users/jinhokim/test/musinsa
COPY . .
ENV DAYS=90 
RUN pip3 install --upgrade \
    boto3
CMD ["iam.py"]
ENTRYPOINT ["python3"]