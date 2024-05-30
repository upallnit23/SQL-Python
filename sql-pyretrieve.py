#2. Advanced Data Analysis in Gym Manaagement System
#Task 1:SQL BETWEEN Usage

from mainsql import connect_database

#Function used to update member information to the database in mySQL
def retrieve_data(cursor, start_age, end_age):
    query = "SELECT id, name, age from Members WHERE age BETWEEN %s AND %s" 
    cursor.execute(query, (start_age, end_age))
    for records in cursor.fetchall():
        print(records)

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        retrieve_data(cursor, 25, 30)

        conn.commit()

    except Exception as e:
        print(f"Error {e}")

    finally:
        cursor.close()
        conn.close()