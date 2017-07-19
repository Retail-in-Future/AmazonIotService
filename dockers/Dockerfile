FROM fedora:25

RUN dnf install -y python-pip
RUN pip install --upgrade pip
RUN pip install django djangorestframework

ENV PROJECT_PATH=/root/project

WORKDIR $PROJECT_PATH
COPY ./ AmazonIotService/

WORKDIR $PROJECT_PATH/AmazonIotService