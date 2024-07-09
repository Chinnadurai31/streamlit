#fv#456
FROM ubuntu:latest
WORKDIR /
COPY . /
CMD ['tail','-f','/dev/null]
