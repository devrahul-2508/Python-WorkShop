import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the CSV File
df = pd.read_csv("dataset.csv")
print(df.head(10))

#Find total number of runs Kohli
total_runs = df["Runs"].sum()
no_of_matches = len(df["Runs"])
print("Total number of runs kohli has scored",total_runs)
print("Total number of matches played by kohli",no_of_matches)

#Average of runs
average_runs = df["Runs"].mean()
print(f"Average score of Kohli in {no_of_matches} matches is {int(average_runs)}")

#Number of matches played at different positions
positions = df[" Pos "].unique()
print(positions)

df[" Pos "] = df[" Pos "].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6",
})


pos_counts = df[" Pos "].value_counts()
print(pos_counts)
pos_values = pos_counts.values
print(pos_values)
pos_labels = pos_counts.index
print(pos_labels)

# fig = plt.figure(figsize=(10,7))
# plt.pie(pos_values,labels=pos_labels)
# plt.show()

def showPlot(key):
    labels = df[key].unique()
    values = df[key].value_counts()
    plt.pie(values,labels=labels)
    plt.show()

def showGroupByPlot(key1,key2):
    sum_values=df.groupby(key1)[key2].sum()
    values=sum_values.values  
    labels = sum_values.index
    plt.pie(values,labels=labels)
    plt.show()
# showPlot(" Opposition    ")
# showPlot(" Ground            ")
# showPlot(" Dismissal ")

#Total runs scored in different positions
# runs=df.groupby(" Pos ")["Runs"].sum()
# runs_values=runs.values
# run_labels=runs.index

# plt.pie(runs_values,labels=run_labels)
# plt.show()
#print(runs)
#showGroupByPlot(" Pos ","Runs")
#showGroupByPlot(" Opposition    "," 6s")

#Total sixes scored with different oppositions


centuries=df.query("Runs>=100")
print(centuries)

innings = centuries[" Inns"]
tons = centuries["Runs"]

plt.bar(innings,tons, color='blue',width=0.2)
plt.show()

#Calculate dismissals of kohli
showPlot(" Dismissal ")

plt.bar(centuries[" Opposition    "],centuries["Runs"], color='blue',width=0.2)
plt.show()
