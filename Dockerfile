FROM alpine

RUN mkdir /app
WORKDIR /app/

COPY . .

ENTRYPOINT ["tail", "-f", "/dev/null"]
