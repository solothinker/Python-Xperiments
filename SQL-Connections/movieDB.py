from getpass import getpass
from mysql.connector import connect,Error

#Making connection with SQL
try:
    with connect(
        host="localhost",
        user=input("User Name: "),
        password = getpass("your password: "),
        ) as connection:
# creating table
        create_movies_tables_query = """
        CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        gener VARCHAR(100),
        collection_in_mil INT
        )
        """
    with connection.cursor() as cursor:
        cursor.execute(create_movies_tables_query)
        connection.commit()
except Error as e:
    print("Current Error",e)
