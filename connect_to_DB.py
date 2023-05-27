import json
import mysql.connector

access = json.load(open("access.json", "r"))

def connect():
    try:
        connection = mysql.connector.connect(
            host = access["host"],
            user = access["user"],
            password = access["password"],
            database = access["database"]
        )
        return connection
    except mysql.connector.Error as error:
        print(f'Error: {error}')
        return 0