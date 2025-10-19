import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="EVA@yasser,123"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()


