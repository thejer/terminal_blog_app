import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    sDATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.sDATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.sDATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.sDATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.sDATABASE[collection].find_one(query)
