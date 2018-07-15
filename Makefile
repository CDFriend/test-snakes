IMAGE_NAME=apache_testsnakes

HTTPD_PORT=8080
RUN_ARGS=--rm -p$(HTTPD_PORT):80

all: run

run: image
	docker run $(RUN_ARGS) $(IMAGE_NAME)

image:
	docker build -t $(IMAGE_NAME) .
