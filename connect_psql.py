import os, subprocess
import psycopg2

no_database = ['postgres', 'admin', 'template1', 'template0']

try:
    connection = psycopg2.connect(
        host="localhost",
        user="admin",
        password="",
        database="admin"

    ) 

    with connection.cursor() as cursor:
        cursor.execute(
            """select datname from pg_database;"""
        )

        db_name_ = list(cursor)
        db_name = []
        
        for i in range(0, len(db_name_)):
            element = db_name_[i]
            
            if element[0] in no_database:
                pass

            else:
                db_name.append(element[0])

except Exception as ex:
    print(ex, "error")

finally:
    if connection:
        connection.close()



