LOAD DATA LOCAL INFILE '/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_Student_Performance_data.csv'
INTO TABLE Performance
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Student_ID, Semester_Name, @Paper_ID, Paper_Name, Marks, Effort_Hours)
set
	Student_ID = CAST(SUBSTRING(TRIM(@Student_ID), 4) AS UNSIGNED),
    Paper_ID = CAST(SUBSTRING(TRIM(@Paper_ID), 5) AS UNSIGNED);
