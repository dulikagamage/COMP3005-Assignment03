# COMP3005-Assignment03

Author: Dulika Gamage
Student Number: 101263208

Program Description: A program that interacts with PostgreSQL to manipulate student data.

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

## Compile    

