#!/bin/bash
SQL_HOST_FROM_CONTAINER=`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_container`
cd ../config
if [ -f .env.api ]
then
    echo "Adding"
    export $(cat ../config/.env.api | grep -v '#' | sed 's/\r$//' | awk '/=/ {print $1}' )
    export SQL_HOST=${SQL_HOST_FROM_CONTAINER}
fi
cd ../api

poetry run ./manage.py "$@"