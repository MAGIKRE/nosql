docker pull mongo
docker run --name my-mongo -p 27017:27017 -d mongo
bash docker/mongo_setup.sh