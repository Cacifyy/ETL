LOAD DATA LOCAL INFILE '/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_Student_Counceling_Information_data.csv'
INTO TABLE Student
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Student_ID, @DOA, @DOB, @Department_Choices, @Department_Admission)
set
	Student_ID = CAST(SUBSTRING(TRIM(@Student_ID), 4) AS UNSIGNED),
    Department_Choices = CAST(SUBSTRING(@Department_Choices, 6) AS UNSIGNED),
    Department_Admission = CAST(SUBSTRING(@Department_Admission, 6) AS UNSIGNED),
    DOB = STR_TO_DATE(@DOB, '%m/%d/%Y'),
    DOA = STR_TO_DATE(@DOA, '%m/%d/%Y'); 
