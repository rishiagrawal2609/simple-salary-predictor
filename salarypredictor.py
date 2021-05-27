# importing important libraries and functions  
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Adding dataset 
data = pd.read_csv("Salary_Data.csv")

# Creating feature variable
x = data['YearsExperience'].values.reshape(-1,1)

# Creating target variable
y = data['Salary']

# Initializing empty model
model = LinearRegression()

# Training Model 
model.fit(x,y)

# model predictions
exp = float(input("Enter the Experience of the person:"))
sal = model.predict([[exp]])
print(f"The employ with experience {exp} will get salary of {sal}")


# Saving weigths for future use
joblib.dump(model,"salarypred.pk1")