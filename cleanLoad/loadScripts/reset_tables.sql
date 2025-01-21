DROP TABLE IF exists Performance;
DROP TABLE IF exists Student;
DROP TABLE IF exists Employee;
DROP TABLE IF exists Department;

CREATE TABLE Department (
	Department_ID INT PRIMARY KEY,
	Department_Name VARCHAR(255) NOT NULL,
	DOE DATE NOT NULL
);



CREATE TABLE Employee (
    Employee_ID INT PRIMARY KEY,
    DOB DATE NOT NULL,
    DOJ DATE NOT NULL,
    Department_ID INT,
    CONSTRAINT FOREIGN KEY (Department_ID) REFERENCES Department (Department_ID)
);

CREATE TABLE Student (
    Student_ID INT,
    DOA DATE NOT NULL,
    DOB DATE NOT NULL,
    Department_Choices INT,
    Department_Admission INT,
    CONSTRAINT PRIMARY KEY (Student_ID, Department_Choices, DOA),
    CONSTRAINT FOREIGN KEY (Department_Choices) REFERENCES Department(Department_ID),
    CONSTRAINT FOREIGN KEY (Department_Admission) REFERENCES Department(Department_ID)

);
CREATE TABLE Performance (
    Student_ID INT,
    Paper_ID INT,
    Semester_Name VARCHAR(50),
    Paper_Name VARCHAR(255),
    Marks INT CHECK (Marks BETWEEN 0 AND 100),
    Effort_Hours INT CHECK (Effort_Hours >= 0),
    CONSTRAINT PRIMARY KEY (Student_ID, Paper_ID, Semester_Name),
    CONSTRAINT FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
);
