import pandas as pd
from datetime import datetime

file_path = '/home/pgill914/ETL-ASG/Data/Department_Information.csv'
df = pd.read_csv(file_path)

def dateValidation(dateTemp):
	if pd.isna(dateTemp) or dateTemp == '':
		return False
	try:
		dateTemp = datetime.strptime(dateTemp, '%m/%d/%Y')
		if dateTemp.year > 1900:
			return True;
		else:
			return False;
	except ValueError:
		return False

#Keep only valid df contents
validRows = df[df['DOE'].apply(dateValidation)]

#Store Invalid aswell
invalidRowDOE = df[~df.index.isin(validRows.index)]
invalidDuplicates = df[df.duplicated(subset=['Department_ID'], keep=False)]

invalidRows = pd.concat([invalidRowDOE, invalidDuplicates])

invalidRows.to_csv('/home/pgill914/ETL-ASG/cleanLoad/invalidData/invalidDepartmentData.csv', index=False)

#Remove Duplicates from Valid rows
validRows = validRows.drop_duplicates(subset=['Department_ID'])
validRows.to_csv('/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_department_data.csv', index=False)

