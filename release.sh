#!/bin/bash
docker_image_name=`echo "docker.retail.com/retail/amazoniot:1.0"`

docker build --rm -t $docker_image_id -f DockerfileProd .
docker push $docker_image_name
# End of script
