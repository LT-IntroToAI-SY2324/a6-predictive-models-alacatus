import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles(000)","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=.2)
#create linear regression model
modl = LinearRegression().fit(xtrain,ytrain)
#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places.
coef = np.around(modl.coef_, 2)
intercept = round(float(modl.intercept_),2)
r_squared = round(modl.score(x,y),2)
 
print("Model's Linear Equation: y=",coef, "x+", intercept)
print("R Squared value:", r_squared)


#Loop through the data and print out the predicted prices and the
#actual prices
predict = modl.predict(xtest)
predict = np.around(predict, 2)


print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    #___change the headers and understand how this works 
    print(f"miles(000): {x_coord[0]} age: {x_coord[1]} Actual: {actual} Predicted: {predicted_y}")

#figure out how to print actual
print(f"Prediction when miles is 89k znd age is 10: {modl.predict([[89,10]])}")
print(f"Prediction when miles is 150k and age is 20: {modl.predict([[150,20]])}")

print("***************")
print("Testing Results")