#!/bin/bash

##########################################################
#         DEFINE FILES AND VARIABLES HERE
##########################################################

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

docker run -i -e DOCKER_HOST_USERID="$(id -u):$(id -g)" --rm $docker_image_id /bin/bash << "EOF"
set -o errexit -o nounset \
\
&& python manage.py test \
EOF

#popd

# End of script