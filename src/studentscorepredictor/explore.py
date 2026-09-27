# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split,cross_val_score
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error
# import joblib


# df = pd.read_csv("../../data/students.csv")

# print(df,"\n")
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.isna().sum())
# print(df.describe())



# correl = df["StudyHours"].corr(df["FinalScore"])
# print(correl)


# print(df.corr())



# x = df[["Age", "StudyHours", "Attendance", "Assignments", "PreviousScore", "SleepHours"]]
# y = df["FinalScore"]

# print(x)
# print(y)

# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# print("xtrain: ", x_train)
# print("xtest: ", x_test)
# print("ytrain: ", y_train)
# print("ytest: ", y_test)

# model = LinearRegression()

# print(model)

# model.fit(x_train,y_train)

# joblib.dump(model,"model.pkl")

# print("Coefficient: ", model.coef_)
# print("intercept: ", model.intercept_)

# predictions = model.predict(x_test)
# print(predictions)

# score = model.score(x_test,y_test)
# print("R2 score: ", score)

# mae = mean_absolute_error(y_test, predictions)
# print("MAE: ", mae)

# mse = mean_squared_error(y_test,predictions)
# print("MSE: ", mse)

# rmse = root_mean_squared_error(y_test, predictions)
# print("RMSE: ", rmse)


# scores = cross_val_score(model,x,y,cv=5)
# print("cross validation sore: ", scores)
# print("mean r2: ", scores.mean())

# residuals = y_test-predictions
# print("Residuals: ", residuals)


# # plt.scatter(df["StudyHours"], df["FinalScore"])

# # plt.xlabel("Study Hours")
# # plt.ylabel("Final Score")
# # plt.title("Study Hours vs Final Score")

# # plt.show()

# # plt.scatter(df["Attendance"], df["FinalScore"])
# # plt.xlabel("Attendance")
# # plt.ylabel("FinalScore")
# # plt.title("Attendance vs final score")

# # plt.show()

# # plt.scatter(df["PreviousScore"],df["FinalScore"])

# # plt.xlabel("Previous Score")
# # plt.ylabel("Finalscore")
# # plt.title("previous score vs final score")

# # plt.show()

# # plt.scatter(df["Assignments"], df["FinalScore"])
# # plt.show()


# # plt.scatter(df["SleepHours"], df["FinalScore"])
# # plt.show()



# # plt.scatter(df["Age"], df["FinalScore"])
# # plt.show()


# plt.scatter(residuals,predictions)
# plt.axhline(0)
# plt.xlabel("residuals")
# plt.ylabel("predictions")
# plt.title("residuals vs predictions")
# plt.show();




import pandas as pd
import matplotlib.pyplot as plt


# 1. Load dataset
df = pd.read_csv("../../data/students.csv")


# 2. Basic information
print("Dataset:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isna().sum())

print("\nStatistical Summary:")
print(df.describe())


# 3. Correlation
print("\nCorrelation Matrix:")
print(df.corr())


# 4. Relationship between individual features and target

# Study Hours vs Final Score
plt.scatter(df["StudyHours"], df["FinalScore"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.show()


# Attendance vs Final Score
plt.scatter(df["Attendance"], df["FinalScore"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.show()


# Previous Score vs Final Score
plt.scatter(df["PreviousScore"], df["FinalScore"])
plt.xlabel("Previous Score")
plt.ylabel("Final Score")
plt.title("Previous Score vs Final Score")
plt.show()


# Assignments vs Final Score
plt.scatter(df["Assignments"], df["FinalScore"])
plt.xlabel("Assignments")
plt.ylabel("Final Score")
plt.title("Assignments vs Final Score")
plt.show()


# Sleep Hours vs Final Score
plt.scatter(df["SleepHours"], df["FinalScore"])
plt.xlabel("Sleep Hours")
plt.ylabel("Final Score")
plt.title("Sleep Hours vs Final Score")
plt.show()


# Age vs Final Score
plt.scatter(df["Age"], df["FinalScore"])
plt.xlabel("Age")
plt.ylabel("Final Score")
plt.title("Age vs Final Score")
plt.show()


# 5. Specific correlation
study_score_corr = df["StudyHours"].corr(df["FinalScore"])

print("\nStudy Hours vs Final Score Correlation:")
print(study_score_corr)

