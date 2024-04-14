import mysql.connector


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahi@nayak186",
        database="employees"
    )


def execute_query():
    connection=connect_to_database()
    cursor=connection.cursor()
    query="SELECT * FROM departments"
    cursor.execute(query)
    rows=cursor.fetchall()

    for row in rows:
        print(row)


if __name__=="__main__":
    execute_query()