sudo docker build -t vacc:v2 .

sudo docker run -d --name vacc_syd vacc:v2 syd

sudo docker run -d --name vacc_adel vacc:v2 adel