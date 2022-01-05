build:
	sh -c 'docker build -t tacobyte .'
start:
	# sh -c 'docker rm tacobyte'
	sh -c 'docker run --name tacobyte -p 8080:80 -itd --privileged --entrypoint /bin/bash --mount src="$(shell pwd)/src",target=/var/www/html,type=bind tacobyte'
	sh -c 'docker exec tacobyte service apache2 start'