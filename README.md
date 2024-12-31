# Project Title

## Project Aim
This project aims to demonstrate a comprehensive data processing pipeline using Data Version Control (DVC) and statistical modeling techniques. The pipeline includes various stages such as data loading, preprocessing, feature engineering, model training, and evaluation to ensure a robust analysis of the dataset.

## Tasks Overview
The following tasks have been completed in this project:
1. **Data Loading**: Raw data is loaded from CSV files using the `load_data.py` script.
2. **Data Preprocessing**: The data is cleaned and preprocessed to handle missing values using the `preprocess.py` script.
3. **Feature Engineering**: New features are created from the processed data using the `feature_engineering.py` script.
4. **Model Training**: A machine learning model is trained using the features with the `train_model.py` script.
5. **Model Evaluation**: The trained model is evaluated, and the results are saved using the `evaluate_model.py` script.
6. **Data Version Control**: DVC is utilized to manage data and model versions throughout the project.
7. **A/B Hypothesis Testing**: A/B hypothesis testing is conducted to evaluate the impact of specific features on key performance indicators (KPIs).

## Task 3: A/B Hypothesis Testing

### Overview
This project conducts A/B hypothesis testing to evaluate the impact of specific features on key performance indicators (KPIs).

### Key Performance Indicators
- Conversion Rate
- Average Profit Margin

### Data Segmentation
- **Group A (Control Group)**: Plans without the feature.
- **Group B (Test Group)**: Plans with the feature.

### Statistical Testing
- Conducted t-tests for numerical KPIs.
- Conducted chi-squared tests for categorical data.

### Results
- T-test results indicated insufficient data for analysis.
- Chi-squared test showed a significant difference in gender distribution between groups.

### Conclusion
The findings suggest that the feature being tested may have different effects based on gender distribution. Further analysis may be needed to explore alternative KPIs or additional features.

## Usage Instructions
To run the project and execute the DVC pipeline, follow these steps:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd week-3
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize DVC (if not already done):
   ```bash
   dvc init
   ```
4. Run the DVC pipeline:
   ```bash
   dvc repro
   ```
This command will execute all stages in order, ensuring that the data is processed, the model is trained, and the evaluation is performed.

## Dependencies
Make sure to install the necessary dependencies listed in `requirements.txt` before running the project.