import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
# print(x)
# print(y)
# Step 2: Standardize the data using StandardScaler, 
scalar = StandardScaler().fit(x)
# Step 3: Transform the data
x = scalar.transform(x)
# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x,y)
# Step 5: Fit the data
modl = linear_model.LogisticRegression().fit(x_train,y_train)
# Step 6: Create a LogsiticRegression object and fit the data

# Step 7: Print the score to see the accuracy of the model
print("Accuracy:", modl.score(x_test, y_test))
print("*************")

for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 3)
    y_pred = int(modl.predict(x))
    x_coord = x_test[index]
    if y_pred == 0:
        y_pred = "Not Purchased"
    elif y_pred == 1:
        y_pred = "Purchased"
    else:
        y_pred = "No result"
    
    actual = y_test[index]
    if actual == 0:
        actual = "Not Purchased"
    elif actual == 1:
        actual = "Purchased"
    else:
        actual = "No result"
    print(" Predicted status: " + y_pred + " Actual status: " + actual)
# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
###^^^ add the x vals to print
