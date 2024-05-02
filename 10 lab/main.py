

import psycopg2
from config import load_config
import psycopg2
from config import load_config

def connect():
    # Load database configuration
    config = load_config()

    # Extract connection details from the configuration dictionary
    host = config['host']
    user = config['user']
    password = config['password']
    dbname = config['dbname']

    # Connect to the database using the extracted details
    return psycopg2.connect(
        host=host,
        user=user,
        dbname=dbname,
        password=password
    )


def create_table():
    try:
        connection = connect()
        with connection.cursor() as cursor:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT,
                phone TEXT
            )
            """
            cursor.execute(create_table_query)
            print("Users table created successfully.")
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Successfully closed connection")

def add_user():
    name = input("Enter user name: ")
    phone = input("Enter user phone: ")
    try:
        connection = connect()
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO users (name, phone) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, phone))
            print("User added successfully.")
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] Successfully closed connection")

def query_users():
    name = input("Enter user name to query (leave blank to query all users): ")
    phone = input("Enter user phone to query (leave blank to query all users): ")
    try:
        connection = connect()
        with connection.cursor() as cursor:
            select_query = "SELECT * FROM users WHERE TRUE"
            if name:
                select_query += f" AND name = '{name}'"
            if phone:
                select_query += f" AND phone = '{phone}'"
            cursor.execute(select_query)
            users = cursor.fetchall()
            print("Users:")
            for user in users:
                print(user)
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Successfully closed connection")

def delete_user():
    name = input("Enter user NAME to delete: ")
    try:
        connection = connect()
        with connection.cursor() as cursor:
            delete_query = f"DELETE FROM users WHERE name = '{name}'"
            cursor.execute(delete_query)
            print("User deleted successfully.")
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] Successfully closed connection")

def main():
    create_table()
    while True:
        print("\nChoose an option:")
        print("1. Add user")
        print("2. Query users")
        print("3. Delete user")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            query_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
