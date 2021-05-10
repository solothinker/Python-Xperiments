from getpass import getpass
from mysql.connector import connect,Error

#Making connection with SQL
try:
    with connect(
        host="localhost",
        user=input("User Name: "),
        password = getpass("your password: "),
        ) as connection:
        dbName = input("Enter new database name: ")
        create_db_query = "CREATE DATABASE "+ dbName
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            
except Error as e:
    print("Current Error",e)


