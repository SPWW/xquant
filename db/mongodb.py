#!/usr/bin/python
"""mongodb"""
import logging
from pymongo import MongoClient
from bson import ObjectId


def get_datetime_by_id(_id):
    """get datetime from _id"""
    return ObjectId(_id).generation_time


class MongoDB:
    """MongoDB"""

    def __init__(self, user, password, db_name, db_url):
        client = MongoClient(db_url)
        self.__client = eval("%s.%s" % (client, db_name))
        self.__client.authenticate(user, password)

    def create_index(self, collection, index):
        self.__client[collection].create_index(index, unique=True)

    def insert_one(self, collection, record):
        """insert_one"""
        logging.debug("mongodb %s insert : %s", collection, record)
        _id = self.__client[collection].insert_one(record).inserted_id
        return _id

    def insert_many(self, collection, records):
        """insert_one"""
        ret = self.__client[collection].insert_many(records)
        return ret

    def update_one(self, collection, _id, record):
        """update_one"""
        logging.debug("mongodb %s(_id=%s) update : %s", collection, _id, record)
        self.__client[collection].update_one({"_id": ObjectId(_id)}, {"$set": record})

    def find(self, collection, query):
        """find"""
        #print(query)
        records = []
        ret = self.__client[collection].find(query)
        for i in ret:
            records.append(i)
        return records
