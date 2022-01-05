# Use ubuntu
FROM ubuntu:latest

# Fix tzdata thing
# ENV TZ=America/Vancouver
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ARG DEBIAN_FRONTEND=noninteractive

# Install dependancies
RUN apt-get update
RUN apt-get install -y tzdata
RUN apt-get install apache2 build-essential php python3 python3-pip -y