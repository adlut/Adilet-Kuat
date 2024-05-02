import psycopg2
from config import load_conf

def connect():
    config = load_conf()

    host = config['host']
    user = config['user']
    password = config['password']
    dbname = config['dbname']
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
                id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
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

def add_user(name, phone):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.callproc("insert_user", (name, phone))
            print("User added successfully.")
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] Successfully closed connection")

def query_users(pattern_name=None, pattern_phone=None):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.callproc("get_users", (pattern_name, pattern_phone))
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

def delete_user(name):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.callproc("delete_user", (name,))
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
            name = input("Enter user name: ")
            phone = input("Enter user phone: ")
            add_user(name, phone)
        elif choice == "2":
            pattern_name = input("Enter part of name (leave blank for all users): ")
            pattern_phone = input("Enter part of phone (leave blank for all users): ")
            query_users(pattern_name, pattern_phone)
        elif choice == "3":
            name = input("Enter user NAME to delete: ")
            delete_user(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
