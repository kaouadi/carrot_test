
###
# Step 1
###
# Build image manishng/python3.10.12sb
docker build -t manishng/python3.10.12sb -f ./Dockerfile_python3.10.12sb .
# Save image python python3.10.12sb
docker push manishng/python3.10.12sb

###
# Step 2
###
# Build image manishng/python3.10.12sb_django4.2.2 
docker build -t manishng/python3.10.12sb_django4.2.2 -f ./Dockerfile_python3.10.12sb_django4.2.2 .
# Save image python manishng/python3.10.12sb_django4.2.2 
docker push manishng/python3.10.12sb_django4.2.2 

###
# Step 3
###
# Build image manishng/python3.10.12sb_django4.2.2_and_carrot:yyyy_mm_dd
docker build -t manishng/python3.10.12sb_django4.2.2_and_carrot:2023_06_19 -f ./Dockerfile_python3.10.12sb_django4.2.2_and_carrot .
# Save image python manishng/python3.10.12sb_django4.2.2_and_carrot:yyyy_mm_dd
docker push manishng/python3.10.12sb_django4.2.2_and_carrot:2023_06_19 


###
# Step 4
###
# Create or restore manually database for example (folder share)
docker compose -f docker-compose-dev.yml run -v ~/Download:/dl  -ti --entrypoint bash  webserver
cd /app
pg_restore -h postgres -d carrotdb -U carrot /dl/bxxxxx.dump



###
# Step 5
###
# Launch of the webserver dev mode 
docker compose -f ./docker-compose-dev.yml up


###
# Step 6
###
# Access to the webserver in mode development 
docker compose -f docker-compose-dev.yml run -ti --entrypoint bash  server

