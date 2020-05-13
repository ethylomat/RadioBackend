# Select Python 3.6 Base-Image
FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Select workdir
ENV APP_ROOT /project
WORKDIR ${APP_ROOT}

# Install packages
RUN apt-get update
RUN pip3 install -U pip
COPY requirements.txt ${APP_ROOT}/requirements.txt
RUN pip3 install -r ${APP_ROOT}/requirements.txt

RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
RUN pip3 install psycopg2

# Set the working directory to /app
WORKDIR ${APP_ROOT}

# Copy the current directory contents into the container at /app
ADD . ${APP_ROOT}

RUN chmod 775 -R ${APP_ROOT}

# Command for testing the server
CMD  ['python3 manage.py collectstatic --noinput', '&&', '/bin/sh','-c','python manage.py runserver']
