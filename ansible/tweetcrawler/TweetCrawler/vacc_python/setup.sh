sudo docker build -t vacc:v1 .

sudo docker run -d --name vacc_melb vacc:v1 melb

sudo docker run -d --name vacc_bris vacc:v1 bris