import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = 'your_file.csv'  # Replace with your file path
    df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

    # Extract specific columns
# Example: Extract 'column1' and 'column2'
extracted_data = df[['column1', 'column2']]

    # Display the extracted data
print(extracted_data)

# Save the extracted data to a new CSV file
output_path = 'extracted_data.csv'  # Replace with desired output file path
extracted_data.to_csv(output_path, index=False)

print(f"Data successfully extracted and saved to {output_path}")