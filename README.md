# basedbin frontend

Frontend for [basedbin](https://github.com/samedamci/basedbin) pastebin-like service server.

## Installing with Docker Compose

### Frontend and server on single machine

* Clone repo to your machine
* Edit `docker-compose.yml` file and set database credentials*
* Run `docker-compose up` command
* Go to `localhost:8080` (or any other port you set for `nginx` service)

\* Do not change services names and `DB_HOST` and `SERVER_HOSTNAME` variables

### Frontend with remote server

* Clone repo to your machine
* Edit `docker-compose.alone.yml` file
* Run `docker-compose -f docker-compose.alone.yml up` command
* Go to `localhost:8080` (or any other port you set for `nginx` service)