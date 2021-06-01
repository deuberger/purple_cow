#/bin/sh
docker-compose down
docker-compose rm
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker rmi purplecow_api
rm -rf /tmp/postgres-data
docker-compose up
