#Gym Database Management with Python and SQL
#Task 4:Delete Workout Session

from mainsql import connect_database

#Function used to remove workout session in the database in mySQL
def delete_workoutsession(session_id):
    query = "DELETE FROM WorkoutSessions WHERE session_id = %s" 
    cursor.execute(query, (session_id))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        delete_workoutsession(7)

        conn.commit()
        print("Workout session deleted.")

    except Exception as e:
        print(f"Error {e}")

    finally:
        cursor.close()
        conn.close()