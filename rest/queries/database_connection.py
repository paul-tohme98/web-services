import mysql.connector


class DatabaseConnection:        
    @classmethod
    def openConnection(self, db_host, db_user, db_password, db_name):        # try:

        # Create a connection to the MySQL database
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
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
        
    @classmethod
    def getClientId(self, cursor, email):
        query = "SELECT client_id FROM clients WHERE email = %s"
        cursor.execute(query, (email,))
        # Fetching the results
        client_id = cursor.fetchone()
        return client_id

    @classmethod
    def getHouseProps(self, cursor, house_address):
        print("Address : ", house_address)
        query = "SELECT * FROM houses WHERE address = %s"
        cursor.execute(query, (house_address,))

        house_props = cursor.fetchone()
        return house_props
    
    @classmethod
    def insertDemand(cls, conn, cursor, client_id, loan_amount, loan_duration, house_id, date_demand, valid):
        try:
            # MySQL INSERT query with parameterized query
            query = """INSERT INTO demands (client_id, loan, duration, house_id, date_demand, valid) VALUES (%s, %s, %s, %s, %s, %s)"""
            
            # Execute the query with the provided parameters
            cursor.execute(query, (client_id, loan_amount, loan_duration, house_id, date_demand, valid,))
            
            # Commit the transaction to make the changes permanent
            conn.commit()
            
            print("Record inserted successfully!")
        except Exception as e:
            # Rollback the transaction in case of any error
            cursor.connection.rollback()
            raise e



    @classmethod
    def getDataForLoanScore(self, cursor, client_id):
        query = "SELECT debts, late_payments, recent_falls FROM properties WHERE client_id = %s"
        cursor.execute(query, (client_id,))
        dataForLoanScore = cursor.fetchone()
        return dataForLoanScore
    
    @classmethod
    def getRevenuData(self, cursor, client_id):
        query = "SELECT yearly_income, yearly_outcome FROM properties WHERE client_id = %s"
        cursor.execute(query, (client_id,))
        revenuData = cursor.fetchone()
        return revenuData

    @classmethod
    def getConformityData(self, cursor, house_id):
        query = "SELECT land_dispute , complies_with_regulations, eligible_for_loan FROM houses WHERE house_id = %s"
        cursor.execute(query, (house_id,))
        conformityData = cursor.fetchone()
        print("Conf Data : ", conformityData)
        return conformityData
    
    @classmethod
    def getEstimation(self, cursor, region, codePostal, surface, nbChambres):
        lowerSurface = float(surface) - 100.0
        upperSurface = float(surface) + 100.0

        query = """SELECT 
                        estimated_value FROM houses 
                        WHERE region = %s 
                        AND code_postal = %s 
                        AND num_of_chambers = %s 
                        AND area between %s and %s"""  # Using placeholders for query parameters
        cursor.execute(query, (region, codePostal, nbChambres, lowerSurface, upperSurface))
        values = cursor.fetchall()
        # Convert fetched values to float
        values = [float(value[0]) for value in values]
        return values

    
    


