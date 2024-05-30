#Gym Database Management with Python and SQL
#Task 2:Add a Workout Session

from mainsql import connect_database

#Function used to add workout session to the database in mySQL
def add_workoutsession(session_id, member_id, session_date, session_time, activity):
    query = "INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (session_id, member_id, session_date, session_time, activity))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        add_workoutsession(9, 1106, "2024-06-01", "14:00", "speed-racing")

        conn.commit()
        print("Member added.")

    except Exception as e:
        print(f"Error {e}")

    finally:
        cursor.close()
        conn.close()


