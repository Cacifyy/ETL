SELECT 'Student_ID','Department_Admission', 'Department_Name', 'Semester_Name','Paper_ID','Marks','Effort_Hours'
UNION ALL
SELECT
    Student_ID,
    Department_Admission,
    Department_Name,
    Semester_Name,
    Paper_ID,
    Marks,
    Effort_Hours
FROM Comprehensive_Data
INTO OUTFILE '/tmp/comprehensive_data.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';






