from pymongo import MongoClient

connection = MongoClient("mongodb://tester:strong_password@localhost:27017/")

# creates new database if not exists
database = connection.get_database("test_db")
