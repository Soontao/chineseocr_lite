# build image
FROM python:3-alpine AS build

RUN apk update && apk upgrade && apk add --no-cache build-base

WORKDIR /app

COPY . .

WORKDIR /app/psenet/pse

RUN make

# run image
FROM python:3-alpine

WORKDIR /app

COPY --from=build /app /app

# install dependency
RUN pip install -r requirements.txt

CMD ["python", "app.py"]


