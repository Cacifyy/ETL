import pandas as pd


def foreign_key_constraint_check (student_data :pd.DataFrame, department_data :pd.DataFrame):

	valid_department_ids = department_data['Department_ID']

	clean_data = student_data[
        student_data['Department_Choices'].isin(valid_department_ids) &
        student_data['Department_Admission'].isin(valid_department_ids)
    ]
	return clean_data


def drop_duplicate (df_clean :pd.DataFrame):

# It finds the duplicate rows of 'Student_ID', 'Paper_ID', 'Semster_Name'
    duplicates_data = df_clean[df_clean.duplicated(subset=['Student_ID', 'Department_Choices', 'DOA'], keep=False)]

    # drop those duplicate rows
    clean_data = df_clean.drop(duplicates_data.index)

    return clean_data


file_path = "/home/pgill914/ETL-ASG/Data/Student_Counceling_Information.csv"
df = pd.read_csv(file_path)

df_depart = pd.read_csv('/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_department_data.csv')

# Check if 'department_admission' exists
if 'Department_Admission' in df.columns:

	valid_rows = []

	for index, row in df.iterrows():
		if pd.isna(row['Department_Admission']):
			print(f"StudentID:: Missing or incorrect data in 'Department_Admission' in 'Student_Counceling_Information'")
		else:
			valid_rows.append(row)

	# Remove rows with missing values
	df_clean = pd.DataFrame(valid_rows)


	df_clean = foreign_key_constraint_check (df_clean, df_depart)

	df_clean = drop_duplicate (df_clean)

	df_clean.to_csv('/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_Student_Counceling_Information_data.csv', index=False)


else:
	print("Exception: department_admission' does not exist in 'Student_Counciling_Information.csv'")
	df_clean = pd.DataFrame()

