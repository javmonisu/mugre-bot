# Database config information set in environmental variables
from os import environ
from pymongo import MongoClient


host = str(environ['MONGO_HOST'])
port = int(environ['MONGO_PORT'])
username = str(environ['MONGO_USERNAME'])
password = str(environ['MONGO_PASSWORD'])


class Database:
    @property
    def connection(self):
        """
        We let MongoClient raise the exceptions.
        In my case, the bot does not work without database.
        """
        client = MongoClient(host, port)
        database = client[str(environ['MONGO_DATABASE'])]
        database.authenticate(name=username, password=password)
        return database

    @property
    def users(self):
        return self.connection['admin_users']

    @property
    def doggos(self):
        return self.connection['doggos']

    @property
    def eccel(self):
        return self.connection['eccelmovil']

    @property
    def gifs(self):
        return self.connection['gif']

# Database initialization, exceptions will by raised by PyMongo
db = Database()
