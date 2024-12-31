
## Business Objective
AlphaCare Insurance Solutions (ACIS) is dedicated to developing cutting-edge risk and predictive analytics in the area of car insurance planning and marketing in South Africa. As a member of the data analytics team, your first project involves analyzing historical insurance claim data. The primary objective of this analysis is to optimize the marketing strategy and identify “low-risk” targets for potential premium reductions, thereby creating opportunities to attract new clients.

### Key Areas of Focus
To achieve these business objectives, you will need to enhance your knowledge and perform analyses in the following areas:

### Insurance Terminologies:
Familiarize yourself with how insurance works by reviewing key insurance terms. A recommended resource is the article "50 Common Insurance Terms and What They Mean" by Cornerstone Insurance Brokers.
### A/B Hypothesis Testing:
Understand the benefits of A/B hypothesis testing. You will be tasked with accepting or rejecting the following null hypotheses:
There are no risk differences across provinces.
There are no risk differences between zip codes.
There are no significant margin (profit) differences between zip codes.
There are no significant risk differences between women and men.
### Machine Learning & Statistical Modeling:
For each zip code, fit a linear regression model to predict total claims.
Develop a machine learning model to predict optimal premium values based on:
Features of the car to be insured.
Features of the owner.
Features related to the owner's location.
Any other relevant features you identify.
### Reporting and Recommendations
Your final report should detail the methodologies used, present findings from your analyses, and make recommendations on plan features that could be modified or enhanced based on the test results. This will assist AlphaCare Insurance Solutions in tailoring their insurance products more effectively to meet consumer needs and preferences.

## Task Overview
### Task 1: Git and GitHub
- **Tasks**: 
  - Create a git repository for the week with a good README.
  - Implement Git version control.
  - Set up CI/CD with GitHub Actions.
- **Key Performance Indicators (KPIs)**:
  - Dev Environment Setup.
  - Relevant skills in the area demonstrated.
  - Project Planning - EDA & Stats.

### Task 2: Data Version Control (DVC)
- **Tasks**:
  - Install DVC: `pip install dvc`.
  - Initialize DVC: `dvc init`.
  - Set up local remote storage.
  - Add your data: `dvc add <data.csv>`.
  - Commit changes to version control.
  - Push data to local remote: `dvc push`.
  
### Task 3: A/B Hypothesis Testing
- **Tasks**:
  - Select Metrics and Data Segmentation.
  - Conduct statistical testing.
  - Analyze and report findings.
  
### Task 4: Statistical Modeling
- **Tasks**:
  - Data preparation: Handle missing data, feature engineering, and encoding categorical data.
  - Model building: Implement various modeling techniques.
  - Model evaluation: Evaluate each model using appropriate metrics.
  - Feature importance analysis: Use SHAP or LIME for interpretability.

## Usage Instructions
To run the project and execute the DVC pipeline, follow these steps:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd week-3
### Install the required dependencies:  
```bash
pip install -r requirements.txt
```
### initalize dvc
```bash
dvc init
### run dvc command
```bash 
dvc repro
This command will execute all stages in order, ensuring that the data is processed, the model is trained, and the evaluation is performed.

Dependencies
Make sure to install the necessary dependencies listed in requirements.txt before running the project.

