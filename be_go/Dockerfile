FROM ubuntu:18.04

LABEL maintainer="meetwithfriendsapp@gmail.com"

WORKDIR /app

EXPOSE 3344

RUN apt update 
RUN apt-get install hugo -y
RUN mkdir db
RUN go build

COPY . /app

CMD [ "./app" ]

