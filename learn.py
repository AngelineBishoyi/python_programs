import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='employee'
)

# Create a cursor object
mycursor = mydb.cursor()

# Now you can execute SQL queries using mycursor.execute() and interact with the database

# Close the cursor and connection when done
mycursor.close()
mydb.close()
