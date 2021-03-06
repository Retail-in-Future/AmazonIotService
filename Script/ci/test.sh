#!/bin/bash

this_script=$(basename $0)
top_dir=$(dirname $0)"/../../"

echo -e "$top_dir"

pushd $top_dir

app_name=$(basename $(pwd))
docker_image_id=`echo "local/${app_name}:latest" | tr "[:upper:]" "[:lower:]"`

docker run -i -e DOCKER_HOST_USERID="$(id -u):$(id -g)" --rm $docker_image_id /bin/bash << "EOF"
set -o errexit -o nounset \
\
&& python3 manage.py test \
EOF

popd

# End of script
