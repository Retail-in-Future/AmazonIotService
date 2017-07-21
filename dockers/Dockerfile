FROM fedora:25

RUN dnf install -y python-pip
RUN pip install --upgrade pip
RUN pip install boto3
RUN pip install django djangorestframework

ENV PROJECT_PATH=/root/project

RUN mkdir ~/.aws/

WORKDIR $PROJECT_PATH
COPY ./ AmazonIotService/

WORKDIR $PROJECT_PATH/AmazonIotService