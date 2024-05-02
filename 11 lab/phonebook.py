import psycopg2
from config import load_config

def connect():
    # Load database configuration
    config = load_config()

    # Extract connection details from the configuration dictionary
    host = config['host']
    user = config['user']
    password = config['password']
    dbname = config['database']  # Adjusted key name

    # Connect to the database using the extracted details
    return psycopg2.connect(
        host=host,
        user=user,
        dbname=dbname,
        password=password
    )

def create_table():
    connection = None
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
    connection = None
    try:
        connection = connect()
        name = input("Enter user name: ")
        phone = input("Enter user phone: ")
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
    connection = None
    try:
        connection = connect()
        name = input("Enter user name to query (leave blank to query all users): ")
        phone = input("Enter user phone to query (leave blank to query all users): ")
        with connection.cursor() as cursor:
            select_query = "SELECT * FROM users WHERE TRUE"
            conditions = []
            params = []
            if name:
                conditions.append("name LIKE %s")
                params.append(f"%{name}%")
            if phone:
                conditions.append("phone LIKE %s")
                params.append(f"%{phone}%")
            if conditions:
                select_query += " AND " + " AND ".join(conditions)
            print("Query:", select_query)  # Debugging statement
            print("Params:", params)  # Debugging statement
            cursor.execute(select_query, params)
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

            



def update_user():
    connection = None
    try:
        connection = connect()
        user_id = input("Enter user ID to update: ")
        name = input("Enter new name (leave blank to keep unchanged): ")
        phone = input("Enter new phone (leave blank to keep unchanged): ")
        with connection.cursor() as cursor:
            update_query = "UPDATE users SET"
            updates = []
            params = []
            if name:
                updates.append("name = %s")
                params.append(name)
            if phone:
                updates.append("phone = %s")
                params.append(phone)
            if updates:
                update_query += " " + ", ".join(updates)
                update_query += " WHERE id = %s"
                params.append(user_id)
                cursor.execute(update_query, params)
                print("User updated successfully.")
            else:
                print("No changes specified.")
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] Successfully closed connection")

def delete_user():
    connection = None
    try:
        connection = connect()
        name = input("Enter user NAME to delete: ")
        with connection.cursor() as cursor:
            delete_query = "DELETE FROM users WHERE name = %s"
            cursor.execute(delete_query, (name,))
            print("User deleted successfully.")
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.commit()
            connection.close()
            print("[INFO] Successfully closed connection")

def query_users_pagination(limit, offset):
    connection = None
    try:
        connection = connect()
        with connection.cursor() as cursor:
            select_query = "SELECT * FROM users LIMIT %s OFFSET %s"
            cursor.execute(select_query, (limit, offset))
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

def delete_user_by_username_or_phone(identifier):
    connection = None
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.callproc('delete_user_by_username_or_phone', [identifier])
            connection.commit()
            print("User deleted successfully.")
    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Successfully closed connection")

def main():
    create_table()
    while True:
        print("\nChoose an option:")
        print("1. Add user")
        print("2. Query users")
        print("3. Update user")
        print("4. Delete user")
        print("5. Query users with pagination")
        print("6. Delete user by username or phone")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            query_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            limit = int(input("Enter the limit: "))
            offset = int(input("Enter the offset: "))
            query_users_pagination(limit, offset)
        elif choice == "6":
            identifier = input("Enter the username or phone number to delete: ")
            delete_user_by_username_or_phone(identifier)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
