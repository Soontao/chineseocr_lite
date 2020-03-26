# run image
FROM python:3.7-slim

WORKDIR /app

# install dependency
RUN apt update
RUN apt install -y python-dev build-essential libsm6 libglib2.0-0 libxext6 libxrender1

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app/psenet/pse

RUN make

WORKDIR /app


WORKDIR /app

CMD ["python3", "app.py"]


