FROM python:3.6-slim
WORKDIR /app
COPY . /app
RUN pip install boto3 dnspython
CMD "python" "updatedns.py" $DOMAIN
