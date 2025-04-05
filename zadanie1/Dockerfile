FROM ubuntu:latest

RUN apt-get update && apt-get install -y fpc

WORKDIR /app
COPY . /app

RUN fpc app.pas

CMD ["./app"]
