import pandas as pd
import datetime as dateime 

# Load the dataset
file_path = 'Assignment1Data_Sample (1).csv'  # Update with actual file path
data = pd.read_csv(file_path)

# Step 1: Remove irrelevant columns
print("\nStep 1: Remove irrelevant columns")
relevant_columns = ['Object ID', 'Department', 'Object Name', 'Title', 'Culture', 'Artist Nationality', 
                    'Object Begin Date', 'Object End Date', 'Medium', 'Credit Line', 'Country']
cleaned_data = data[relevant_columns]
print(cleaned_data.head())  # Show result in terminal
cleaned_data.to_csv('cleaned_data_step1.csv', index=False)  # Save output

# Step 2: Handle missing values in required fields
print("\nStep 2: Handle missing values in required fields")
required_columns = ['Object ID', 'Department', 'Object Name', 'Title', 'Culture', 
                    'Object Begin Date', 'Object End Date', 'Medium']
missing_before = cleaned_data.isnull().sum()  # Log missing values before cleaning
cleaned_data = cleaned_data.dropna(subset=required_columns)
missing_after = cleaned_data.isnull().sum()  # Log missing values after cleaning
print(f"Missing values before cleaning:\n{missing_before}\n")
print(f"Missing values after cleaning:\n{missing_after}\n")
cleaned_data.to_csv('cleaned_data_step2.csv', index=False)  # Save output

# Step 3: Ensure consistency in categorical data formatting
print("\nStep 3: Ensure consistency in categorical data formatting")
cleaned_data['Department'] = cleaned_data['Department'].str.title()
cleaned_data['Culture'] = cleaned_data['Culture'].str.title()
cleaned_data['Medium'] = cleaned_data['Medium'].str.title()
print(cleaned_data[['Department', 'Culture', 'Medium']].head())  # Show result in terminal
cleaned_data.to_csv('cleaned_data_step3.csv', index=False)  # Save output

# Step 4: Logical consistency check (Object Begin Date <= Object End Date)
print("\nStep 4: Logical consistency check (Begin Date <= End Date)")
invalid_dates = cleaned_data[cleaned_data['Object Begin Date'] > cleaned_data['Object End Date']]
if not invalid_dates.empty:
    print(f"Rows with invalid date ranges:\n{invalid_dates[['Object ID', 'Object Begin Date', 'Object End Date']]}")
cleaned_data = cleaned_data[cleaned_data['Object Begin Date'] <= cleaned_data['Object End Date']]
print(cleaned_data[['Object Begin Date', 'Object End Date']].head())  # Show result in terminal
cleaned_data.to_csv('cleaned_data_step4.csv', index=False)  # Save output

# Step 5: Remove duplicate rows based on 'Object ID'
print("\nStep 5: Remove duplicate rows")
duplicates_before = cleaned_data.duplicated(subset=['Object ID']).sum()
cleaned_data = cleaned_data.drop_duplicates(subset=['Object ID'])
duplicates_after = cleaned_data.duplicated(subset=['Object ID']).sum()
print(f"Duplicates before: {duplicates_before}, Duplicates after: {duplicates_after}")
cleaned_data.to_csv('cleaned_data_step5.csv', index=False)  # Save output

# Step 6: Ensure correct date format for 'Object Begin Date' and 'Object End Date'
print("\nStep 6: Ensure correct date format")

# Convert 'Object Begin Date' and 'Object End Date' to datetime, coerce invalid formats to NaT (Not a Time)
cleaned_data['Object Begin Date'] = pd.to_datetime(cleaned_data['Object Begin Date'], errors='coerce').dt.date
cleaned_data['Object End Date'] = pd.to_datetime(cleaned_data['Object End Date'], errors='coerce').dt.date

# Check if there are any invalid dates (i.e., NaT values after coercion)
invalid_dates = cleaned_data[cleaned_data['Object Begin Date'].isna() | cleaned_data['Object End Date'].isna()]
if not invalid_dates.empty:
    print(f"Rows with invalid date formats:\n{invalid_dates[['Object ID', 'Object Begin Date', 'Object End Date']]}")
else:
    print("All dates are in correct format.")

# Optionally, drop rows with invalid dates, or handle them as needed
cleaned_data = cleaned_data.dropna(subset=['Object Begin Date', 'Object End Date'])  # Drop rows with invalid dates

# Save the final cleaned data after date format check
cleaned_data.to_csv('cleaned_data_step6.csv', index=False)  # Save output
print("\nFinal cleaned data after date format check")
print(cleaned_data.head())  # Show result in terminal



# Log actions and save the final result
log_file_path = 'data_cleaning_log.txt'
with open(log_file_path, 'w') as log_file:
    log_file.write("Data Cleaning Log:\n")
    log_file.write("1. Removed irrelevant columns.\n")
    log_file.write("2. Handled missing values in required fields.\n")
    log_file.write("3. Ensured consistency in categorical data formatting.\n")
    log_file.write("4. Checked for logical inconsistencies in dates.\n")
    log_file.write("5. Removed duplicate rows based on Object ID.\n")
    log_file.write("6. Ensured date format for Object begin date and Object end date.\n")
    
    

# Final cleaned data
print("\nStep 6: Final cleaned data")
print(cleaned_data.head())  # Show result in terminal
cleaned_data.to_csv('final_cleaned_data.csv', index=False)  # Save final cleaned data
