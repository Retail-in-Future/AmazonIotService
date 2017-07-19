#!/bin/bash

this_script=$(basename $0)
top_dir=$(dirname $0)"/../../"
echo -e "$top_dir"

##########################################################
#              DEFINE FUNCTIONS HERE
##########################################################

##########################################################
#               BEGINNING OF MAIN
##########################################################

pushd $topdir

app_name=$(basename $(pwd))
docker_image_id=`echo "local/${app_name}:latest" | tr "[:upper:]" "[:lower:]"`
docker build -t $docker_image_id -f dockers/Dockerfile .

#popd

# End of script