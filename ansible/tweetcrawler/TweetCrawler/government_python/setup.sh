sudo docker build -t government:v1 .

sudo docker run -d --name government_melb government:v1 melb

sudo docker run -d --name government_bris government:v1 bris