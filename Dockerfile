FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /webAppFlask
WORKDIR webAppFlask
RUN pip install Flask
ENTRYPOINT ["python"]
CMD ["run2.py"]


