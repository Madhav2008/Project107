import csv
import pandas as pd
import plotly.express as px

file = pd.read_csv("StudentData.csv")
mean = file.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
print(mean)
fig = px.scatter(mean, x = "student_id", y = "level", size = "attempt", color = "attempt")
fig.show()
