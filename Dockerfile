# build image
FROM python:3.7-alpine AS build

RUN apk update && apk upgrade && apk add --no-cache build-base

WORKDIR /app

COPY . .

WORKDIR /app/psenet/pse

RUN make

# run image
FROM python:3-slim

WORKDIR /app

COPY --from=build /app /app

# install dependency
RUN apt update
RUN apt install -y python-dev build-essential
RUN pip install -r requirements.txt

CMD ["python", "app.py"]


