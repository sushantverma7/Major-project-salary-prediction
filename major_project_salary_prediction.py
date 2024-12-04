import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os
import re

# File path to the dataset
file_path = r"C:\Users\admin\OneDrive\Desktop\python2\salary_converted.csv"

# Step 1: Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    exit()

# Step 2: Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except pd.errors.ParserError as e:
    print("Error reading the CSV file. Please check the file format.")
    raise e

# Step 3: Inspect the dataset
print("First few rows of the dataset:")
print(data.head())

# Step 4: Normalize column names
data.rename(columns=lambda x: x.strip().lower(), inplace=True)

if 'experience' not in data.columns or 'salary' not in data.columns:
    print("Error: 'experience' or 'salary' column not found in the dataset.")
    exit()

# Step 5: Preprocess the 'experience' column
def preprocess_experience(exp):
    """
    Extract numeric values from experience strings.
    E.g., "1 year" -> 1, "1-2 year" -> 1, "3 year" -> 3
    """
    if pd.isna(exp):
        return None
    match = re.search(r'\d+', exp)
    return int(match.group()) if match else None

data['experience'] = data['experience'].apply(preprocess_experience)

# Convert 'salary' to numeric and handle errors
data['salary'] = pd.to_numeric(data['salary'], errors='coerce')

# Drop rows with missing or invalid values
data = data.dropna(subset=['experience', 'salary'])

# Check if dataset is empty after cleaning
if data.empty:
    print("Error: No valid data available after cleaning.")
    exit()

print(f"Dataset size after cleaning: {data.shape}")

# Step 6: Split data into features and target
X = data[['experience']]  # Predictor
y = data['salary']        # Target

# Split the data into training and testing sets
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Data split into training and testing sets successfully!")
except ValueError as e:
    print("Error during train-test split. Ensure dataset has enough samples.")
    raise e

# Step 7: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Predictions and evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Display results
print(f"Coefficient: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
print(f"Mean Squared Error: {mse}")

# Step 9: User input for salary prediction
try:
    user_experience = float(input("Enter years of experience: "))  # User input for experience
    new_experience = pd.DataFrame([[user_experience]], columns=['experience'])  # Convert input to DataFrame
    predicted_salary = model.predict(new_experience)
    print(f"Predicted Salary for {user_experience} years of experience: {predicted_salary[0]}")
    print("\n\n   THE PROJECT IS MADE BY  \n1.Sushant verma \n2.Vansh\n3.Asad khan")
except ValueError:
    print("Invalid input. Please enter a valid number for years of experience.")

