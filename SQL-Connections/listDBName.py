from getpass import getpass
from mysql.connector import connect,Error

#Making connection with SQL
try:
    with connect(
        host="localhost",
        user=input("User Name: "),
        password = getpass("your password: "),
        ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
##            
except Error as e:
    print("Current Error",e)
