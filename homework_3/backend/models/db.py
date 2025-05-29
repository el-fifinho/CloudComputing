import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create and return a database connection."""
    try:
        connection = mysql.connector.connect(
            host='34.118.52.224',
            user='flaskuser',  
            password='flaskuser',
            database='videosite'
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    """Close the database connection."""
    if connection and connection.is_connected():
        connection.close()
        print("Connection closed.")

def store_translation(youtube_url, original_text, translated_text, lang):
    """Store a translation in the database."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO translations (youtube_url, original_text, translated_text, language)
        VALUES (%s, %s, %s, %s)
        """
        try:
            cursor.execute(insert_query, (youtube_url, original_text, translated_text, lang))
            connection.commit()
            print(f"Translation for {youtube_url} stored successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(connection)

def fetch_translation(youtube_url, lang):
    """Fetch a translation from the database."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        select_query = """
        SELECT translated_text FROM translations WHERE youtube_url = %s AND language = %s
        """
        try:
            cursor.execute(select_query, (youtube_url, lang))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                print("No translation found for this video.")
                return None
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(connection)
