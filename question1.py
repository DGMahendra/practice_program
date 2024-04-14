import mysql.connector

# Function to connect to MySQL database
def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahi@nayak186",
        database="employees"
    )

# Function to execute SQL query and fetch results
def fetch_employees():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    query = "SELECT * FROM departments"
    cursor.execute(query)

    rows = cursor.fetchall()  # Fetch all rows
    for row in rows:
        yield row

    cursor.close()
    connection.close()

for employee in fetch_employees():
    print(employee)