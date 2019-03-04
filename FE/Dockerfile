FROM node:8.10

LABEL maintainer="meetwithfriendsapp@gmail.com"

RUN mkdir /usr/src/webapp
WORKDIR /usr/src/webapp

ENV PATH /usr/src/webapp/node_modules/.bin:$PATH

COPY package.json /usr/src/webapp/package.json
RUN npm install
RUN npm install -g @angular/cli@1.7.1

COPY . /usr/src/webapp

CMD ng serve --host 0.0.0.0
