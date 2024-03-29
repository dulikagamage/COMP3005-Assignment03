# COMP3005-Assignment03

#### Author: Dulika Gamage
#### Student Number: 101263208

## Video Demonstration:
https://youtu.be/Ae-0KgVG7DE
## Program Description: 
  A program that interacts with PostgreSQL to manipulate student data.
  ### Functions:
  #### controlFlow():  
  Executes the program and manages the user input.  
  #### mainMenu():  
  Prints the main menu to the screen.  
  #### getAllStudents():  
  Prints all students from the database to the screen.  
  #### addStudent(first_name, last_name, email, enrollment_date):  
  Adds a new student to the database with all student info.  
  #### updateStudentEmail(student_id, new_email):  
  Finds student by id and updates email with the new given email.  
  #### deleteStudent(student_id):  
  Finds student by id and deleted student from the database.  
## How to use the program:
  Ensure PostgreSQL is running on your localhost.   
  In pgAdmin4, create a database called "Assignment03"  
  Run the following query to create the table:  
  
      CREATE TABLE students (
        student_id serial PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL,
        email text NOT NULL UNIQUE,
        enrollment_date date
      );
  
  Then run another query to insert some initial data:  
  
      INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
      ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
      ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
      ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

## Compiling and Running:
  Verify that you have Python by running the following command in your terminal:
  
      python --version
  Also, install the following if you do not have it already. In your terminal enter:
  
      pip3 install psycopg2  
  Navigate to the directory in which the a3.py file is stored.  
  Enter the following into your command prompt or terminal:
  
      python a3.py  
  
## Once Running:
  Once the program is running you can follow the instructions given in the console.   
  You may also reference my video for a demo.
