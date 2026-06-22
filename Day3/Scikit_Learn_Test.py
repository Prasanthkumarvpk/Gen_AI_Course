# # If we train 100% data it will predict all the questions correctly 
# # instead we use 80% data is to train and 20% data is to test.

# # 100 records == students
# # 80 records == train
# # 20 records == test

# # 1) train_test_split :

# from sklearn.model_selection import train_test_split

# x= [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# y= [[10],[20],[30],[40],[50],[60],[70],[80],[90],[100]]

# # # random_state is used to block the random array data generation if you resume every file run it will generate a random array data

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=52)

# print("X_train", x_train)
# print("Y_train", y_train)
# print("X_test", x_test)
# print("Y_test", y_test)

# # 2) Linear Regression : Oka input (X) ki output (y) madhya relationship ni nerchukuni future values predict cheyyadam.
# #          ⬇️
#     # Straight Line Graph ==> ONLY Numerical Data 

# # If you want to use other data it should be encoded to numerical data

# # Series = Single column = []  | Series  → Numerical + Text + Dates + Categories

# # Wrong Code : here two columns 
# from sklearn.linear_model import LinearRegression
# import pandas as pd

# data = {
#     "Experience" : [1,2,3,4,5],
#     "Salary" : [20000,30000,40000,50000,60000]
# }

# df = pd.Series(data)

# X = df["Experience"]
# y = df["Salary"]

# model = LinearRegression()

# model.fit(X,y)

# prediction = model.predict([6])

# print(prediction)

# # Correct Code : 

# import pandas as pd

# experience = pd.Series([1,2,3,4,5])

# print(experience)


# # DataFrame = Rows & Columns = [[]] | DataFrame → Numerical + Text + Dates + Categories

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["John","David","Mike"],
#     "Age": [22,25,28],
#     "Salary": [30000,40000,50000],
#     "Is_Employee": [True,True,False]
# })

# print(df)

# from sklearn.linear_model import LinearRegression
# import pandas as pd

# data = {
#     "Experience" : [1,2,3,4,5],
#     "Salary" : [20000,30000,40000,50000,60000]
# }

# df = pd.DataFrame(data)

# X = df[["Experience"]]
# y = df["Salary"]

# model = LinearRegression()

# model.fit(X,y)

# prediction = model.predict([[6]])

# print(prediction)

# # 3) Model Evalution : Comparing Actual Data(Marks) to Predicted Data(Marks)

#     # How to check model predicting correct answers : By Using

#         # 1) MAE (Mean Absolute Error) : Most beginner-friendly metric. [MAE = Average of Errors]

#                 # Example:   Actual	    Predicted        Errors         Average 
#                 #             100	        90             10       [sum of errors/no.of errors]
#                 #             80	        70             10       (10+10+10)/3 = 10
#                 #             60	        50             10
#                 #           "Here MAE == 10"

# from sklearn.metrics import mean_absolute_error
# import pandas as pd

# actual = [100,80,60]

# predicted = [90,70,50]

# MAE = mean_absolute_error(
#     actual, predicted
# )

# print(MAE)


# 1. Split Data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import math

# Dataset
X = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y = [10,20,30,40,50,60,70,80,90,100]

# 80% Train, 20% Test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=52
)

print("X_train:", X_train)
print("y_train:", y_train)
print("X_test :", X_test)
print("y_test :", y_test)

# 2. Train Model

model = LinearRegression()

model.fit(X_train, y_train)

# 3. Predict Test Data

y_pred = model.predict(X_test)

print("\nPredicted Values:", y_pred)

# 4. Evaluate Model

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

# rmse = mean_squared_error(
#     y_test,
#     y_pred,
#     squared=False
# )
rmse = math.sqrt(mse)

print("\nMAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)

# 5. Predict Future Value

future_prediction = model.predict([[11]])

print("\nPrediction for X=11 :", future_prediction)


import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "Experience": [1,2,3,4,5],
    "Skills": [2,3,4,5,6],
    "Salary": [20000,30000,40000,50000,60000]
})

X = df[["Experience", "Skills"]]

y = df["Salary"]

model = LinearRegression()

model.fit(X, y)

from sklearn.linear_model import LinearRegression

X = [1,2,3,4]
y = [5,10,15,20]

model = LinearRegression()

model.fit(
    [[x] for x in X],
    y
)

print(model.predict([[6]]))


