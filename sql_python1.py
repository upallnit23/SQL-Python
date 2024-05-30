#Gym Database Management with Python and SQL
#Task 1:Add a Member

from mainsql import connect_database

#Function used to add members to the database in mySQL
def add_member(id, name, age):
    query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, name, age))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        add_member(1109, "Judy Smelsie", 34)

        conn.commit()
        print("Member added.")

    except Exception as e:
        print(f"Error {e}")

    finally:
        cursor.close()
        conn.close()


