from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from utils import mongo_connection, db_connection, conf

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_connection

# Relational database initialisation
sql_db = SQLAlchemy(app)


# creating a model for mysql
class User(sql_db.Model):

    __tablename__ = "users"

    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.String(50))
    firstname = sql_db.Column(sql_db.String(50))


# Nosql database initialisation
cluster = MongoClient(mongo_connection)

# Choose the database in the cluster
mongo_db = cluster[conf['mongo_name']]

# Create or choose a collection in the database
mongo_collection = mongo_db['my_collection']

# mongo_collection.insert_one({"name": "mebale", "firstname": "noel", "age": 23})

if __name__ == "__main__":
    app.run(debug=True)
