import joblib
import pandas as pd

model = joblib.load("model.pkl")

age = float(input("enter your age: "))
study_hours = float(input("enter study hours: "))
attendance = float(input("enter your attendance: "))
previous_score = float(input("enter previous score: "))
assignments = float(input("enter assignments: "))
sleep_hours = float(input("enter sleephours: "))

student = pd.DataFrame([{
    "Age": age,
    "StudyHours": study_hours,
    "Attendance": attendance,
    "Assignments": assignments,
    "PreviousScore": previous_score,
    "SleepHours": sleep_hours
}])

prediction = model.predict(student)

print("Predicted Final Score: ", prediction[0])
