FROM python:3.8

# store in /project
WORKDIR /project

# copy requirements.txt into container's /project/
ADD . /project

# install nodejs
RUN apt-get update && apt-get install -y curl && \
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \
apt-get install -y nodejs

# isntall python lib
RUN pip install -r requirements.txt

EXPOSE 2889

RUN npm install

RUN npm run build:stage

CMD ["python","main.py"]
