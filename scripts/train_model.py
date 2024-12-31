import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Train a model
# Replace 'data/features.csv' with the actual path to your features file

def train_model():
    data = pd.read_csv('data/features.csv')
    X = data.drop('target', axis=1)  # Replace 'target' with your target variable
    y = data['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    # Save the trained model
    joblib.dump(model, 'models/trained_model.pkl')
    print('Model trained and saved successfully.')

if __name__ == '__main__':
    train_model()
