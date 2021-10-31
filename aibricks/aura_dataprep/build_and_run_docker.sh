#!/bin/bash
# This script builds the Docker image with the corresponding
# gRPC scripts, runs it and start listening on port 8061.

IMAGE="aura_dataprep"

echo "* Build Docker image."
docker build . -t bbaldassari/$IMAGE 

echo "* Checking if a previous Docker image is running."
docker_id=$(docker ps | grep $IMAGE | cut -f1 -d\ )
if [[ $docker_id != "" ]]; then
    echo "  - Stop running Docker image $docker_id."
    docker stop $docker_id
else
    echo "  - Found no docker image."
    echo "    Listing $IMAGE:"
    docker ps | grep $IMAGE
fi

echo "* Run Docker image."
docker run -p 8061:8061 bbaldassari/$IMAGE &
sleep 2

echo "* Run client python test script."
source ../env/bin/activate
pytest test_$IMAGE.py
pytest_result=$?

echo "* Stop the Docker image."
docker_id=$(docker ps | grep $IMAGE | cut -f1 -d\ )
if [[ $docker_id != "" ]]; then
    echo "  - Stop running Docker image $docker_id."
    docker stop $docker_id
else
    echo "  - Found no docker image."
    echo "    Listing $IMAGE:"
    docker ps | grep $IMAGE
    docker ps | grep $IMAGE | cut -f1 -d\ 
fi

exit $pytest_result