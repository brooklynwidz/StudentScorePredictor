import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import(mean_absolute_error, mean_squared_error, root_mean_squared_error)


df = pd.read_csv("../../data/students.csv")

x = df[["Age", "StudyHours","Attendance", "Assignments", "PreviousScore", "SleepHours"]]

y = df["FinalScore"]

xtrain, xtest, ytrain, ytest = train_test_split(x,y,train_size=0.2,random_state=40)

model = LinearRegression()

model.fit(xtrain,ytrain)

predictions = model.predict(xtest)

r2 = model.score(xtest,ytest)
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)


print("Model Evaluation")
print("----------------")
print("R2 Score:", r2)
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

joblib.dump(model,"model.pkl")

print("\nModel Saved Successfully")

