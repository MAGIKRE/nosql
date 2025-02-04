-docker pull redis
docker run --name my-redis -d redis
docker ps
docker exec -it my-redis redis-cli