import joblib

# loading saved weights

model = joblib.load("salarypred.pk1")

# model predictions
exp = float(input("Enter the Experience of the person:"))
sal = model.predict([[exp]])
print(f"The employ with experience {exp} will get salary of {sal}")