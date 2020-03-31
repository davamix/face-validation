# Face validation

Use the face as a password

## Preparing data
Generate the embeddings for the user image with the script in *utils/save_embeddings.py*. Change the username and image path if needed.

Copy the database generated, *users.db*, into *app/data/users.db*.

## Build
```
docker-compose build
```

## Run
```
docker-compose up flask
```

Navigate to http://127.0.0.1:5000/login