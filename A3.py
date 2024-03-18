import psycopg2 as ps2

conn = ps2.connect(
                        database = "test", # edit here
                        user = "postgres", # edit here
                        password = "password", # edit here
                        host= 'localhost',
                        port = 5433)

cur = conn.cursor()

# display table
def getAllStudents():
    # execute the INSERT statement
    cur.execute("SELECT * FROM students;")
    for row in cur.fetchall():
        print(row[0], ' |', row[1], '   |', row[2], '   |', row[3], '   |', row[4])
    print("\n")

# insert into table
def addStudent(first_name, last_name, email, enrollment_date):
    sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
    try:
        cur.execute(sql,(first_name, last_name, email, enrollment_date))
    except:
        print("email already exist")
    conn.commit()

# update table
def updateStudentEmail(student_id, new_email):
    sql = "UPDATE students SET email = %s WHERE student_id = %s;"
    cur.execute(sql, (new_email, student_id))
    conn.commit()

# delete in table
def deleteStudent(student_id):
    sql = "DELETE FROM students WHERE student_id = %s;"
    cur.execute(sql, (student_id,))
    conn.commit()

cur.close
conn.close

# getAllStudents()
# addStudent("a","b","c","2023-02-02")
# getAllStudents()
# deleteStudent("4")
# updateStudentEmail("3","a")
# getAllStudents()