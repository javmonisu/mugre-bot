[![Build Status](https://travis-ci.org/dmonter/mugre-bot.svg?branch=master)](https://travis-ci.org/dmonter/mugre-bot)

# @TheMugrestBot

A fancy telegram bot.

```
The bot does things - M. Rajoy, 2018
```

## Basic information

Bot created using pyTelegramBotAPI connected to a database in Mongo.

## Getting started

### Manual installation

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


### Docker

Build the docker image:

```
docker build -t <whatever>/mugre-bot .
```

Run it in on background mode:

```
docker run -d -e MONGO_HOST='' -e MONGO_PORT='' -e MONGO_USERNAME='' -e MONGO_PASSWORD='' -e MONGO_DATABASE='' -e BOT_TOKEN='' <whatever>/mugre-bot
```


