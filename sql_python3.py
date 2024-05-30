#Gym Database Management with Python and SQL
#Task 3:Updating Member Information

from mainsql import connect_database

#Function used to update member information to the database in mySQL
def update_member_age(member_id, age):
    query = "UPDATE Members SET age = %s WHERE member_id = %s" 
    cursor.execute(query, (member_id, age))

conn = connect_database()
if conn:
    try:
        cursor = conn.cursor()
        update_member_age(25, 1101)

        conn.commit()
        print("Member age updated.")

    except Exception as e:
        print(f"Error {e}")

    finally:
        cursor.close()
        conn.close()