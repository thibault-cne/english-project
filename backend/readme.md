# Backend

## Start the backend service

You have to start the database first which came with a phpmyadmin panel.
To start the database you have a docker compose file;

``` bash
docker-compose up
```

Then you can start the backend service with :

``` bash
go run cmd/server/main.go
```
