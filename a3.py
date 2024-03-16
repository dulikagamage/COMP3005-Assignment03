import psycopg2
import sys

hostname = 'localhost'
database= 'Assignment03'
username = 'postgres'
password = 'dulika16'
port_id = 5432

conn = None
cur = None

table_name = 'students'


def getAllStudents():
    try:
        #connect to db
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id
        )
        cur = conn.cursor()

        #create query and execute it
        query = f'SELECT * FROM {table_name};'
        cur.execute(query)
        #get the info from db
        students = cur.fetchall()

        #print all students to screen
        for stu in students:
            print(stu)
        print('\n')

    except Exception as error:
        print (error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    try:
        #connect to db
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id
        )
        cur = conn.cursor()

        #create query and execute it
        query = f''' INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s); '''
        cur.execute(query, (first_name, last_name, email, enrollment_date))
        
        #commit the changes to db
        conn.commit()

        print("Student has been added!")

    except Exception as error:
        print (error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def updateStudentEmail(student_id, new_email):
    try:
        #connect to db
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id
        )
        cur = conn.cursor()

        #create query and execute it
        query = "UPDATE students SET email = %s WHERE student_id = %s"
        cur.execute(query, (new_email, student_id))

        #commit the changes to db
        conn.commit()

        print("Email address updated successfully!")

    except Exception as error:
        print (error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def deleteStudent(student_id):
    try:
        #connect to db
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id
        )
        cur = conn.cursor()

        #create query and execute it
        query = "DELETE FROM students WHERE student_id = %s"
        cur.execute(query, (student_id,))

        #commit the changes to the db
        conn.commit()

        print("Student deleted successfully!")

    except Exception as error:
        print (error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def mainMenu():
    print("Main Menu: \n (1) Print all Students \n (2) Add a Student \n (3) Update a Student Email \n (4) Delete a Student \n (0) Exit \n")

def controlFlow():
    while True: #loop until user chooses to exit

        #prompt user and get user input for selection
        mainMenu()
        choice = input("Enter your selection: ")

        if choice == "1":
            #call addStudents (no info needed from user)
            getAllStudents()

        elif choice == "2":

            #prompt user for information and call addStudent()
            fn = input("Enter student first name: ")
            ln = input("Enter student last name: ")
            e = input("Enter student email: ")
            d = input("Enter student enrollment date (yyyy-mm-dd): ")
            addStudent(fn,ln,e,d)

        elif choice == "3":

            #prompt user for id and new email and call updateStudentEmail()
            id = input("Enter student id: ")
            new_e = input("Enter new student email: ")
            updateStudentEmail(id, new_e)

        elif choice == "4":

            #prompt user for id and call deleteStudent()
            id = input("Enter student id: ")
            deleteStudent(id)

        elif choice == "0":

            #exit program
            print("Exiting program....\n")
            sys.exit(0)

        else:

            #user input invalid
            print("\nThe choice you entered is invalid, please try again.\n")


def main():
    controlFlow()

main()