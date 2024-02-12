import mysql.connector


class DatabaseConnection:        
    @staticmethod
    def openConnection():
        print("Inside openConnection")
        # try:
        # Replace these values with your MySQL database credentials
        host = "127.0.0.1"
        user = "root"
        password = "password"
        database = "bank"  # Change this to the name of your database

        print("conn initialization")
        # Create a connection to the MySQL database
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        print("Connection opened")
        return conn, cursor  # Returning a tuple of connection and cursor
        # except Exception as e:
        #     return {"error": str(e)}
        
    # Close the cursor and connection when done
    @classmethod
    def closeConnection(self, cursor, conn):
        try:
            cursor.close()
            conn.close()
            print("Connection closed")
            return
        except Exception as e:
            return {"error": str(e)}
