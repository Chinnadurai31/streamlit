##
FROM ubuntu:latest
WORKDIR /
COPY . /
CMD ['tail','-f','/dev/null]
