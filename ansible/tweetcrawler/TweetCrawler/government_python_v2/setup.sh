sudo docker build -t government:v2 .

sudo docker run -d --name government_syd government:v2 syd

sudo docker run -d --name government_adel government:v2 adel