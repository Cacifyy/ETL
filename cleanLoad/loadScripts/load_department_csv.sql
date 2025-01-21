LOAD DATA LOCAL INFILE '/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_department_data.csv'
INTO TABLE Department
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Department_ID, Department_Name, @DOE)
SET
DOE = STR_TO_DATE(@DOE, '%m/%d/%Y'),
Department_ID = CAST(SUBSTRING(@Department_ID, 6) AS UNSIGNED);
