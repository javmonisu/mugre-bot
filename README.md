# @TheMugrestBot

A fancy telegram bot.

```
The bot does things - M. Rajoy, 2018
```

## Basic information

Bot created using pyTelegramBotAPI connected to a database in Mongo.

## Getting Started

Install the requirements:

```
pip3 install -r requirements.txt
```

Set your environment variables in the .env file.

```
export MONGO_HOST=''
export MONGO_PORT=''
export MONGO_USERNAME=''
export MONGO_PASSWORD=''
export MONGO_DATABASE=''
export BOT_TOKEN=''
```

Export the file to set the variables and run the run.py file.


# DOCKER

Build the docker image

```
docker build -t eltrolado/mugre-bot .
```

Run the docker image

```
docker run -ti -e MONGO_HOST='' -e MONGO_PORT='' -e MONGO_USERNAME='' -e MONGO_PASSWORD='' -e MONGO_DATABASE='' -e BOT_TOKEN='' eltrolado/mugre-bot 
```
