# Employee-Attrition
Creating a Machine learning model to predict Employee Attrition in a company Using Python and other machine learning algorithms

# Employee Attrition Analysis - Company X

## Introduction
Employee attrition refers to the natural loss of employees through processes such as retirement, resignation, position elimination, personal health issues, or other similar reasons. This reduction in workforce size and strength can lead to increased job duties for the remaining employees, potentially resulting in lower productivity for the company.

This project aims to investigate the reasons for employee attrition at Company X by addressing the following key questions:
1. Why are employees prone to leave the company?
2. What type of employees are leaving?
3. Which employee is likely to leave the company next?

These questions are addressed by examining employee records contained in the dataset and applying machine learning techniques to predict future employee churn. This approach will ultimately help the employer take proactive steps to tackle worker attrition.

## Datasets
The employee datasets from Company X consist of two main parts:
1. **Existing Employees**: 11,428 samples with 10 attributes.
2. **Employees Who Have Left**: 3,571 samples with 10 attributes.

The combined dataset includes a total of 14,999 samples, each with the same 10 attributes.

## Methodologies

### 1. Data Exploration and Visualization (Using Tableau)
Data exploration and visualization are critical for understanding the factors leading to increased employee attrition rates. This approach is useful for answering the questions "Why are employees prone to leave the company?" and "What type of employees are leaving?"

#### Steps:
- Compare the existing and ex-employee datasets based on given attributes using charts.
- Use Tableau to visualize, tell stories, and gain insights into the data based on the following attributes:
  - `satisfaction_level`
  - `last_evaluation`
  - `number_project`
  - `average_monthly_hours`
  - `time_spend_company`
  - `work_accident`
  - `promotion_last_5years`
  - `departments`
  - `salary`

#### Findings:
- Employees with 5 years of tenure tend to leave more, possibly due to fewer promotions.
- Employees with a low number of projects (2) left more.
- Employees with 6 and 7 projects left, possibly due to being overloaded with work.
- The sales department has the highest number of existing and churning employees.
- Most employees receive medium or low salaries.
- Employees with working hours above 285 hours left, while those with moderate hours stayed.
- Employees who received promotions in the last 5 years did not leave.
- Few employees experienced work accidents.

### 2. Building a Machine Learning Prediction Model (Using Python)
To predict which employees are prone to leave next, machine learning techniques were applied.

#### Steps:
1. Extract the 3,571 datasets of employees who have left and assign a target value of '1' to each row.
2. Group the 11,428 samples of existing employees into three clusters based on satisfaction level and last evaluation using cluster analysis in Python:
   - High Satisfaction and High Evaluation: Likely to stay.
   - High Satisfaction and Low Evaluation: Less likely to stay.
   - Low Satisfaction and Moderate Evaluation: Unlikely to stay.
3. Extract the dataset of employees with high satisfaction and performance (1,584 samples) and assign a target value of '0' to each row.
4. Concatenate the two dataframes (total of 5,155 employees) and clean the dataset.
5. Train the new dataset using the K-Nearest Neighbors (KNN) algorithm, iterating K values from 1 to 50.
6. Validate the model and fit the datasets of other existing employees into the built model.
7. The model predicts 3,569 employees who are prone to leave.

### Visualization
Use Tableau to better visualize the predicted data and gain further insights.

## Conclusion
This project provides a comprehensive approach to understanding and predicting employee attrition at Company X. By leveraging data exploration, visualization, and machine learning, the company can take informed actions to reduce attrition and improve employee retention.

## Installation and Usage
1. **Data Exploration and Visualization**: Use Tableau to visualize the provided datasets.
2. **Machine Learning Model**: Follow the steps outlined above using Python libraries such as pandas, scikit-learn, and matplotlib.

## Dependencies
- Python 3.x
- pandas
- scikit-learn
- matplotlib
- Tableau

## Author
Emmanuel Oyedeji
