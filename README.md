# ETL
Overview

This project involves creating and managing a small database using MariaDB and performing data mining tasks using Python and Jupyter Notebook. The goal is to transform raw data into meaningful insights and predictions through the ETL (Extract, Transform, Load) process and statistical analysis.

Project Components

    Database Creation: Load the given CSV files into MariaDB and create a relational database based on the provided ER-Diagram.
    
    Data Transformation and Cleansing: Extract, clean, and transform the raw data to address quality issues and make it 
    suitable for further analysis.
    
    Descriptive and Predictive Analytics:
        Perform descriptive data mining to uncover patterns and insights.
        Build a predictive model using linear regression to forecast student performance in future assignments.

Software Requirements

    MariaDB: To create and manage the relational database.
    Python: For data analysis and predictive modeling.
    Jupyter Notebook: For interactive data mining and visualization.
    Required Python Libraries:
        pandas
        numpy
        matplotlib
        seaborn
        scikit-learn

Part 1: Load Data into MariaDB

    1. Import the CSV files into MariaDB.
    2. Create tables based on the schema described in the ER-Diagram.
    3. Ensure primary and foreign key constraints are properly defined.

Part 2: Data Transformation and Cleansing

    1. Validation Checks:
        Completeness: Check for missing values and report exceptions.
        Validity: Ensure proper data types, date ranges, and key integrity.
        Consistency: Validate relationships between tables using primary and foreign keys.
        Uniqueness: Check for duplicate entries and report issues.
        
    2. Transform Data:
      a. Aggregate and join data as needed.
      b. Create a cleaned dataset ready for analysis.

    3. Handle Specific Exceptions:
        Remove or report invalid entries as per the validation requirements outlined in the project description.

Part 3: Descriptive Analytics

    1. Use Jupyter Notebook to perform descriptive analytics on the transformed data.
    2. Visualize insights using libraries like matplotlib and seaborn.
    3. Document patterns and trends in the data.

Part 4: Predictive Analytics

    1. Use the historical performance data to build a linear regression model:
        Input: Effort (hours spent on an assignment).
        Output: Predicted score.
    2. Train and validate the model using scikit-learn.
    3. Predict the scores for specific students (e.g., SID20131151, SID20149500, SID20182516) assuming 10 hours of effort.

Part 5: Reporting

    1. Generate a report summarizing:
        a. Data cleansing efforts and exceptions identified.
        b. Descriptive analytics findings.
        c. Predictive model results.
    2. Include visualizations and tables to support your conclusions.



