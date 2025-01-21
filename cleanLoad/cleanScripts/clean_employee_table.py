import pandas as pd
from datetime import datetime

df = pd.read_csv('/home/pgill914/ETL-ASG/Data/Employee_Information.csv')

def dateValidation(dateTemp):
	if pd.isna(dateTemp) or dateTemp == '':
		return False
	try:
		datetime.strptime(dateTemp, '%m/%d/%Y')
		return True;
	except ValueError:
		return False

#Keep only valid df contents
validRows = df[df['DOB'].apply(dateValidation)]
validRows = validRows[validRows['DOJ'].apply(dateValidation)]

#Store Invalid aswell
invalidRowDOE = df[~df.index.isin(validRows.index)]
invalidDuplicates = df[df.duplicated(subset=['Employee ID'], keep=False)]

invalidRows = pd.concat([invalidRowDOE, invalidDuplicates])

invalidRows.to_csv('/home/pgill914/ETL-ASG/cleanLoad/invalidData/filtered_Employee_Information_Data.csv', index=False)

#Remove Duplicates from Valid rows
validRows = validRows.drop_duplicates(subset=['Employee ID'])
validRows.to_csv('/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_Employee_Information_Data.csv', index=False)

