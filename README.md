# @TheMugrestBot [![Build Status](https://travis-ci.org/dmonter/mugre-bot.svg?branch=master)](https://travis-ci.org/dmonter/mugre-bot)

A fancy telegram bot (using [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)) connected to a Mongo database. This repo autobuilds the master branch via Travis-CI and pushes it to Docker HUB.

> The bot does things - M. Rajoy, 2018

## Getting started

### Manual installation

Create a virtual environment in your folder and activate it:

```
python -m venv venv
source venv/bin/activate
```

Install the requirements:

```
pip install -r requirements.txt
```

Set your environment variables manually or using [autoenv](https://github.com/kennethreitz/autoenv) in the .env file.

```
export MONGO_HOST=''
export MONGO_PORT=''
export MONGO_USERNAME=''
export MONGO_PASSWORD=''
export MONGO_DATABASE=''
export BOT_TOKEN=''
```

Run the bot:
```
python run.py
```

### Docker

Build the docker image:

```
docker build -t <whatever>/mugre-bot .
```

Run it in on background mode:

```
docker run -d -e MONGO_HOST='' -e MONGO_PORT='' -e MONGO_USERNAME='' -e MONGO_PASSWORD='' -e MONGO_DATABASE='' -e BOT_TOKEN='' <whatever>/mugre-bot
```
