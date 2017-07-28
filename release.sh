#!/bin/bash
docker build --rm -t docker.retail.com/retail/amazoniot:1.0 -f DockerfileProd .
docker push docker.retail.com/retail/amazoniot:1.0
# End of script
