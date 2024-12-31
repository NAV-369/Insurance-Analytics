import pandas as pd

# Preprocess the data
# Replace 'data/processed_data.csv' with the actual path to your processed data file

def preprocess_data():
    data = pd.read_csv('data/processed_data.csv')
    # Example preprocessing: handling missing values
    data.fillna(method='ffill', inplace=True)
    # Save the preprocessed data to a new CSV file
    data.to_csv('data/feature_data.csv', index=False)
    print('Data preprocessed successfully.')

if __name__ == '__main__':
    preprocess_data()
