EPOCH ?= 0
VERSION ?= dev

docker_registry = docker.retail.com
docker_repository = retail
image_base_name = amazoniot
image_tag = $(EPOCH).$(VERSION)
remote_image_name = $(docker_registry)/$(docker_repository)/$(image_base_name)
remote_image_full_name = $(remote_image_name):$(image_tag)

default: image
image:

release:
    docker build --rm -t $(remote_image_full_name) .
	docker push $(remote_image_full_name)
	docker tag $(remote_image_full_name) $(remote_image_name):latest
	docker push $(remote_image_name):latest