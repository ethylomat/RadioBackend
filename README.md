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

Example:
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

## API-Documentation

The API is documented at Swagger.

[API Documentation (v1.1.0)](https://app.swaggerhub.com/apis-docs/AwesomeRadio/radio-backend/1.1.0/)

API Response Example for `https://radio.ethylomat.de/api/v1/channels`:
```json
[
  {
    "id": 0,
    "frequency": 0.1,
    "title": "Konrad Zuse entwickelt Z3",
    "description": "Konrad Zuse entickelte 1941 den ersten funktionierenden Digitalrechner der Welt.",
    "media_url": "https://radio.ethylomat.de/1.mp3"
  }
]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)