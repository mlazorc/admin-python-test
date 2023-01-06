from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
import certifi


connection_string="mongodb+srv://tricomarc:Jolape.2388k@antucluster.obselfs.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:

        '''load_dotenv(find_dotenv())
        password = os.environ.get('MONGODB_PWD')'''
        client = MongoClient(connection_string, tlsCAFile=ca)
        db = client['antuapp']
    except ConnectionError:
        print("Error de conexión con la base de datos")
    return client



