CREATE TABLE Comprehensive_Data AS
SELECT  s.Student_ID, s.Department_Admission,
	d.Department_Name,
	p.Semester_Name, p.Paper_ID, p.Marks, p.Effort_Hours
From Student s
JOIN Department d on s.Department_Admission = d.Department_ID
JOIN Performance p ON s.Student_ID = p.Student_ID;


