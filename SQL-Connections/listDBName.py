# showing the list of database
# Hiding user name and password
from getpass import getpass
import config
from mysql.connector import connect,Error

#Making connection with SQL
try:
    with connect(
        host="localhost",
        user=config.username,
        password =config.password,
        ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
##            
except Error as e:
    print("Current Error",e)
