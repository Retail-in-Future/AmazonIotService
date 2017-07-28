FROM fedora:25

RUN dnf install -y python3-pip
RUN dnf install -y gcc-c++
RUN dnf install -y python-devel
RUN pip3 install --upgrade pip
RUN pip3 install boto3
RUN pip3 install setuptools
RUN pip3 install django djangorestframework mock

ENV PROJECT_PATH=/root/project

RUN mkdir /root/.aws/
COPY config/* /root/.aws/

WORKDIR $PROJECT_PATH
COPY ./ AmazonIotService/

WORKDIR $PROJECT_PATH/AmazonIotService