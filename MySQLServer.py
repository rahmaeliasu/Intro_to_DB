import mysql.connector

try:
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="592072@MySQL"
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    cursor.close()
    connection.close()
    print("MySQL connection closed.")
