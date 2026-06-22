import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Experience": [1,2,3,4,5,6,7,8],
    "Skills": [2,3,4,5,6,7,8,9],
    "Salary": [25000,30000,35000,45000,55000,65000,75000,90000]

})

X = df[["Experience", "Skills"]]
y= df["Salary"]

model = LinearRegression()

model.fit(X,y)

model.predict([[9,10]])
plt.plot(df["Experience"], df["Salary"], marker="o")
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.DataFrame({
    "Experience": [1,2,3,4,5,6,7,8],
    "Skills": [2,3,4,5,6,7,8,9],
    "Salary": [25000,30000,35000,45000,55000,65000,75000,90000]
})

X = df[["Experience", "Skills"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Predictions:", y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

new_data = [[6, 7]]  # Experience=6, Skills=7

prediction = model.predict(new_data)

print("Predicted Salary:", prediction)


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    "Experience": [1,2,3,4,5,6,7,8],
    "Salary": [20000,25000,30000,40000,50000,60000,70000,80000],
    "Hire": [0,0,0,0,1,1,1,1]
})

X = df[["Experience", "Salary"]]
y = df["Hire"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predictions:", y_pred)

acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.DataFrame({
    "Experience": [1,2,3,4,5,6,7,8],
    "Salary": [20000,25000,30000,40000,50000,60000,70000,80000],
    "Hire": [0,0,0,0,1,1,1,1]
})

X = df[["Experience", "Salary"]]
y=df["Hire"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Predictions:",y_pred)

acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)