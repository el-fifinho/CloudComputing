import mysql.connector
from mysql.connector import Error

def test_connection():
    """Test connection to Cloud MySQL."""
    try:
        # Replace with your actual Cloud SQL credentials
        connection = mysql.connector.connect(
            host='34.118.52.224',  # e.g., '127.0.0.1' for local, or 'your-project-id:region:instance-id' for Cloud SQL
            user='flaskuser',         # Your Cloud SQL username
            password='flaskuser', # Your Cloud SQL password
            database='videosite'      # The name of your database
        )

        if connection.is_connected():
            print("Successfully connected to the database")

            # You can test with a simple query to ensure everything works
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to the database: {record}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the connection if it was established
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    test_connection()
