FROM python:3.8

# store in /project
WORKDIR /project

# copy requirements.txt into container's /project/
ADD . /project

# isntall python lib
RUN pip install -r requirements.txt

# install nodejs
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm                       # note this one


EXPOSE 2889

RUN npm install

RUN npm run build:stage

CMD ["python","main.py"]
