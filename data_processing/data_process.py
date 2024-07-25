import pandas as pd
# data_processing.py

def process_data(input_file, output_file):
    # Read the dataset
    df = pd.read_csv(input_file)

    # Perform data processing (example: calculate total sales per invoice)
    df['TotalSales'] = df['Quantity'] * df['UnitPrice']

    # Drop rows with "Unspecified" country
    df = df[df['Country'] != 'Unspecified']

    # Save the processed data
    df.to_csv(output_file, index=False)

    # Return the processed DataFrame
    return df # Added this line to return the df

if __name__ == "__main__":
    df = process_data('Online Retail.csv', 'processed_data.csv') # Assign returned df to a variable

df.head(10)
print(f"Number of rows: {df.shape[0]}")