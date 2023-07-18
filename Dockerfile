# base image
FROM python:3.10
# setup environment variable
ENV DockerHOME=/P13_Python-OC-Lettings-FR/Docker
ARG git_hash=latest
ARG git_branch=""

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# creation of virtual environment
RUN python -m venv env

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip
RUN ./env/bin/pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME

# change image value in docker-compose.yml
RUN sed -i "s/latest/$git_branch-$git_hash/" docker-compose.yml

# run this command to install all dependencies
RUN ./env/bin/pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# start server
CMD ./env/bin/python manage.py makemigrations
CMD ./env/bin/python manage.py migrate
CMD ./env/bin/python manage.py collectstatic
CMD ./env/bin/python manage.py runserver 0.0.0.0:8000