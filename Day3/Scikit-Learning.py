# Scikit Learn is a Python Machine Learning library
# used for data preprocessing, training machine learning
# models, evaluation, and prediction.

# First Scikit Learn Program : pip install scikit-learn

# 1) Supervised Learning : 

# a) Linear Regression : Straight Line Representation

# Linear Regression is a supervised learning
# algorithm used to predict continuous values.

from sklearn.linear_model import LinearRegression

experience = [[1],[2],[3],[4],[5]]

salary = [
    20000,
    30000,
    40000,
    50000,
    60000
]

model = LinearRegression()  # model == Algorithm

model.fit(                  # fit --> Learning Phase
    experience,   
    salary
)

print(model.predict([[6]]))  # Predicted Output : 7000 (predict --> Exam Phase)

from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y=[20, 30, 40, 50, 60]

model = LinearRegression()

model.fit(
    X,y
)

print(model.predict([[7],[10],[14]]))

# Train-Test Split :

# 1000 employee records unayi

# Direct ga anni train cheyyakunda:
# 80% → Training Data
# 20% → Testing Data

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Overfitting : 

# Nuvvu school exam ki prepare avuthunnav anuko.

# Teacher:

# Question:
# What is Python?

# Answer:
# Python is a programming language.

# Nuvvu aa answer ni batti patti memorize chesav.

# Exam lo same question vachindi.

# 100/100 marks

# Kani exam lo ila adigaru:

# Explain the uses of Python.

# Nuvvu answer cheppalekapoyav.

# Enduku?

# Concept nerchukoledu

# Answer ni batti pattavu

# Idi exactly:

# Overfitting : It occurs when a model memorizes the training data instead of learning patterns.

from sklearn.metrics import accuracy_score

actual = [1,1,0,1,1]
predicted = [1,1,1,1,1]

acc = accuracy_score(
    actual,
    predicted
)
print(acc)

# Next Concept: Confusion Matrix

# Most beginners ask:

# Accuracy 80% undi kada,
# inka Confusion Matrix enduku?

# Because Accuracy sometimes lies 😄

# Confusion Matrix Structure

# Binary Classification:

#            Predicted

#           Yes    No   # TP => True Positive, FN => False Negative, FP => False Positive, TN => True Negative

# Actual
# Yes       TP     FN    

# No        FP     TN

from sklearn.metrics import confusion_matrix

actual = [1,1,0,0,1]
predicted = [1,0,0,0,1]

cm = confusion_matrix(
    actual,
    predicted
)

print(cm)

# Let's calculate step by step.

# Actual

# [1, 1, 0, 0]

# Predicted

# [1, 0, 0, 1]

# Compare one by one:

# Actual	Predicted	Result
# 1	1	TP ✅
# 1	0	FN ✅
# 0	0	TN ✅
# 0	1	FP ✅

# Now count:

# TP = 1

# TN = 1

# FP = 1

# FN = 1

# Your answer:

# TP = 2 ❌
# TN = 1 ✅
# FP = 1 ✅
# FN = 0 ❌
# Super Easy Memory Trick

# Think:

# Actual = Reality

# Predicted = Model Guess
# TP
# Reality = Yes

# Guess = Yes

# Correct Yes

# TN
# Reality = No

# Guess = No

# Correct No

# FP
# Reality = No

# Guess = Yes

# Wrong Yes

# FN
# Reality = Yes

# Guess = No

# Wrong No

# b) Logistic Regression :  



