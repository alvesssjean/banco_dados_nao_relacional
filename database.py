from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27018"

client = MongoClient(MONGO_URL)

db = client["aula_nosql2"]

cars_collection = db["cars"]

sales_collection = db["sales"]


