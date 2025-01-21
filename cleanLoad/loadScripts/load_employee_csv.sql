LOAD DATA LOCAL INFILE '/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_Employee_Information_Data.csv'
INTO TABLE Employee
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Employee_ID, @DOB, @DOJ, @Department_ID)
SET
    Employee_ID = CAST(SUBSTRING(TRIM(@Employee_ID), 3) AS UNSIGNED),
    Department_ID = CAST(SUBSTRING(TRIM(@Department_ID), 6) AS UNSIGNED),
    DOB = STR_TO_DATE(@DOB, '%m/%d/%Y'),
    DOJ = STR_TO_DATE(@DOJ, '%m/%d/%Y');
