import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../../data/students.csv")

print(df,"\n")
print(df.shape)
print(df.columns)
print(df.info())
print(df.isna().sum())
print(df.describe())



correl = df["StudyHours"].corr(df["FinalScore"])
print(correl)


print(df.corr())



plt.scatter(df["StudyHours"], df["FinalScore"])

plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")

plt.show()

plt.scatter(df["Attendance"], df["FinalScore"])
plt.xlabel("Attendance")
plt.ylabel("FinalScore")
plt.title("Attendance vs final score")

plt.show()

plt.scatter(df["PreviousScore"],df["FinalScore"])

plt.xlabel("Previous Score")
plt.ylabel("Finalscore")
plt.title("previous score vs final score")

plt.show()

plt.scatter(df["Assignments"], df["FinalScore"])
plt.show()


plt.scatter(df["SleepHours"], df["FinalScore"])
plt.show()



plt.scatter(df["Age"], df["FinalScore"])
plt.show()





