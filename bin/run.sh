#!/usr/bin/env bash
docker stop tornado_starter
docker rm tornado_starter
docker run \
       	-d \
       	--name tornado_starter \
       	-p 10004:8000 \
       	-e DEBUG=${STORAGE_DEBUG} \
        -e DATABASE_URL=${STORAGE_DATABASE_URL} \
       	tornado_starter:latest python manage.py runserver