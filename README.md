# flask-docker-hello-world
This is the repo created for Flask-Hello-World Lab assignment for Security Analysis MSBX 5500.

"ping", "word" and "string-count" routes were included.

# a docker-compose command to run Flask container
```bash
docker-compose up
This command builds my own docker container
```

# a docker-compose command to execute make-request.py within a running container
```bash
docker-compose exec web python make-request.py
```
