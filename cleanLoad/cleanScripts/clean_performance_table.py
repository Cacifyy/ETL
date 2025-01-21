import sys
import pandas as pd

def check_mark(data: pd.DataFrame):

    # Filters clean_data to include only rows where Marks is between 0 and 100.
    clean_data = data[data['Marks'].between(0, 100)]

    # Filters clean_data to include only rows where Marks is NOT between 0 and 100.
    filtered_data = data[~data['Marks'].between(0, 100)]
    
    
    return clean_data, filtered_data

def check_hours(data: pd.DataFrame, filtered_data: pd.DataFrame):
    
    max_int_value = sys.maxsize
    
    # Converts the Effort_Hours column to a numeric data type, if it is not numeric type set the value to 'NaN'
    data.loc[:, 'Effort_Hours'] = pd.to_numeric(data['Effort_Hours'], errors='coerce')
    
    # Creates tmp_filtered_data as a subset of rows where Effort_Hours is NaN.
    tmp_filtered_data = data[data['Effort_Hours'].isna()]
    
    # Removes rows where Effort_Hours is NaN from original data and name it as clean_data.
    clean_data = data.dropna(subset=['Effort_Hours'])
    
    # Concatenates the removed rows to all removed rows
    filtered_data = pd.concat([filtered_data, tmp_filtered_data], ignore_index=True)
    
    # Filters clean_data to include only rows where Effort_Hours is between 0 and max_value.
    clean_data = clean_data[clean_data['Effort_Hours'].between(0, max_int_value)]

    # Creates tmp_filtered_data as rows where Effort_Hours is NOT between 0 and max_value.
    tmp_filtered_data = data[~data['Effort_Hours'].between(0, max_int_value)]

    # Concatenates them again
    filtered_data = pd.concat([filtered_data, tmp_filtered_data], ignore_index=True)

    return clean_data, filtered_data

def check_sid_pids(data: pd.DataFrame, filtered_data: pd.DataFrame):

    # It finds the duplicate rows of 'Student_ID', 'Paper_ID', 'Semster_Name' 
    duplicates_data = data[data.duplicated(subset=['Student_ID', 'Paper_ID', 'Semster_Name'], keep=False)]

    # drop those duplicate rows
    clean_data = data.drop(duplicates_data.index)

    # concate the duplicate rows for reocerds
    filtered_data = pd.concat([filtered_data, duplicates_data], ignore_index=True)

    return clean_data, filtered_data

def check_missing (data: pd.DataFrame, filtered_data: pd.DataFrame):

    # creating a data frame only contains those has missing value
    missing_data = data[data.isnull().any(axis=1)]

    # drops the missing value rows from data
    clean_data = data.dropna()

    # concate the duplicate rows for reocerds
    filtered_data = pd.concat([filtered_data, missing_data], ignore_index=True)

    return clean_data, filtered_data

def check_foreign_key_constraint (data: pd.DataFrame, filtered_data: pd.DataFrame):

    student_data = pd.read_csv('/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_Student_Counceling_Information_data.csv')

    valid_student_ids = student_data['Student_ID']

    clean_data = data[data['Student_ID'].isin(valid_student_ids)]

    removed_row = data[~data['Student_ID'].isin(valid_student_ids)]

    filtered_data = pd.concat([filtered_data, removed_row], ignore_index=True)

    return clean_data, filtered_data

if __name__ == '__main__':

    data = pd.read_csv('/home/pgill914/ETL-ASG/Data/Student_Performance_Data.csv')

    clean_data, filtered_data = check_mark (data)

    clean_data, filtered_data = check_hours (clean_data, filtered_data)

    clean_data, filtered_data = check_sid_pids (clean_data, filtered_data)

    clean_data, filtered_data = check_foreign_key_constraint (clean_data, filtered_data)
    print("Export to csv for student perforamce")
    clean_data.to_csv('/home/pgill914/ETL-ASG/cleanLoad/validData/cleaned_Student_Performance_data.csv', index=False)

    filtered_data.to_csv('/home/pgill914/ETL-ASG/cleanLoad/invalidData/filtered_Student_Performance_Data.csv', index=False)
