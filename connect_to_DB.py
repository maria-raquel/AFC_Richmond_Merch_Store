import json
import mysql.connector

access = json.load(open("access.json", "r"))

def connect():
    connection = mysql.connector.connect(
        host = access["host"],
        user = access["user"],
        password = access["password"],
        database = access["database"]
    )

    print("foi") # botar try except
    return connection

connect()