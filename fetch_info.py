#2. Advanced Data Analysis in Gym Manaagement System
#Task 1:SQL BETWEEN Usage

from mainsql import connect_database

#Make connection
conn = connect_database
if conn is not None:
    try:
        cursor = conn.cursor()

        #Query
        query = "SELECT * from Members WHERE age BETWEEN 25 AND 30"

        #Query search
        cursor.execute(query)

        #Displaying query results
        for record in cursor.fetchall():
            print(record)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

