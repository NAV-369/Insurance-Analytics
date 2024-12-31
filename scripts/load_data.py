import pandas as pd

# Load raw data from CSV
# Replace 'data/raw_data.csv' with the actual path to your raw data file

def load_data():
    raw_data = pd.read_csv('data/raw_data.csv')
    # Save the processed data to a new CSV file
    raw_data.to_csv('data/processed_data.csv', index=False)
    print('Data loaded and processed successfully.')

if __name__ == '__main__':
    load_data()
