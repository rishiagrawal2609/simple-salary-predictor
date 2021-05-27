# Simple Salary Predictor

## This is the model created using the simple linear regression.

 ## This repo contains executable file format of the code ideal for the containers.

 # File Description

- [Salary_Data.csv](Salary_Data.csv)<br>
    The Dataset which is used to train this model. <br>
    RangeIndex: 30 entries, 0 to 29 <br>
    Data columns (total 2 columns): <br>
    
    |#|Column|Non-Null Count|Dtype|
    |-|-|-|-|  
    |0|YearsExperience|30 non-null|float64|
    |1|Salary|30 non-null|float64|
    
    dtypes: float64(2)<br>
    memory usage: 608.0 bytes<br>

- [salarypredictor.py](salarypredictor.py) <br>
    This is the executable file, which takes one input years of Experience and give the output of salary.

- [salarypred.pk1](salarypred.pk1) <br>
    This file conatins the weights that are saved during the model training.
 
- [salpred.py](salpred.py) <br>
    The file contains the code to load saved model and predicting using that model
    