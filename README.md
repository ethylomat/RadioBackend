![coverage](https://gitlab.com/awesomeradio/backend/badges/master/coverage.svg?job=coverage)
![coverage](https://gitlab.com/awesomeradio/backend/badges/master/coverage.svg?job=coverage)

# AwesomeRadio Backend

This is the Backend-Server of the AwesomeRadio project. The AwesomeRadio project is a beginners practical at the Faculty of Mathematics and Computer Science at Heidelberg University.

The backend is responsible for serving the media files and information to different frontends. In the AwesomeRadio project we have a virtual radio frontend and an old radio that will be used as frontend (Raspberry Pi fetching the server).

## Installation

You need Docker and Docker-Compose to run the images:

```bash
$ apt-get update
$ apt-get install docker docker-compose
```

Clone the project:

```bash
$ git clone git@gitlab.com:awesomeradio/backend.git
```

## Usage

```bash
$ cd backend
$ sudo docker-compose up
```

## Environment Variables

The following environment variables should be set in a .env file in the project root.

```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
DJANGO_SETTINGS_MODULE=backend.settings
DJANGO_ADMIN_USER=admin
DJANGO_ADMIN_EMAIL=admin
DJANGO_ADMIN_PASSWORD=admin
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)