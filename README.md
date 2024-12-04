# Major-project-salary-prediction
MAJOR ML PROJECT->SALARY PREDICTION
# Salary Prediction Project

This project is a Python-based implementation of a *Salary Prediction System* using *Linear Regression*. It predicts the salary of an employee based on their years of experience. The project demonstrates the use of basic machine learning concepts and Python libraries like Pandas and scikit-learn.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Workflow](#project-workflow)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to provide an accurate prediction of salaries using a simple linear regression model. It includes the following features:

- Cleaning and preprocessing the dataset.
- Training and testing a Linear Regression model.
- User input functionality to predict salaries based on experience.

## Dataset

The dataset used in this project contains the following columns:

- Emp no: Employee number (unique identifier).
- Employee name: Name of the employee.
- pre company: Previous company of the employee.
- experience: Number of years of experience (e.g., "1 year", "3 years").
- salary: Current salary of the employee.

### Dataset Cleaning:

- The experience column is preprocessed to extract numeric values.
- Rows with missing or invalid data in experience and salary columns are removed.

## Requirements

Make sure to install the following Python libraries before running the project:

- *pandas*
- *scikit-learn*

To install the required libraries, run:

bash
pip install pandas scikit-learn


## Usage

1. Clone the repository to your local machine:

bash
git clone https://github.com/yourusername/salary-prediction.git


2. Navigate to the project directory:

bash
cd salary-prediction


3. Place your dataset file (salary_converted.csv) in the project directory.
4. Run the script:

bash
python salaryprediction.py


5. Enter the years of experience when prompted to predict the salary.

## Project Workflow

1. *Dataset Loading*:

   - Load the CSV file containing employee data.
   - Handle missing or invalid values.

2. *Data Preprocessing*:

   - Normalize column names.
   - Extract numeric values from the experience column.

3. *Model Training*:

   - Split the dataset into training and testing sets.
   - Train a Linear Regression model using scikit-learn.

4. *Model Evaluation*:

   - Evaluate the model using Mean Squared Error (MSE).

5. *Prediction*:

   - Accept user input for years of experience.
   - Predict the corresponding salary using the trained model.

## Results

- *Model Coefficients*:

  - Coefficient: Represents the expected salary increment per year of experience.
  - Intercept: The base salary with zero years of experience.

- *Sample Prediction*:

  
  Enter years of experience: 5
  Predicted Salary for 5 years of experience: 61120.07
  

## Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

TEAM MEMBERS INVOLVED 1. SUSHANT 2. VANSH 3. ASAD
