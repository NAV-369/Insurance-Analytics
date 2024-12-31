import pandas as pd

# Feature engineering
# Replace 'data/feature_data.csv' with the actual path to your feature data file

def feature_engineering():
    data = pd.read_csv('data/feature_data.csv')
    # Example feature engineering: creating a new feature
    data['new_feature'] = data['existing_feature'] * 2  # Replace with your logic
    # Save the features to a new CSV file
    data.to_csv('data/features.csv', index=False)
    print('Features engineered successfully.')

if __name__ == '__main__':
    feature_engineering()
