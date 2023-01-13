import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ploting(dataset, key):
    count = dataset[key].value_counts()
    values = count.values
    label = count.index

    fig = plt.figure(figsize=(10,7))
    plt.pie(values, labels=label)
    plt.show()

dataset = pd.read_csv('data.csv')

runs = dataset.groupby('Pos')['Runs'].sum()
total_runs = dataset['Runs'].sum()
total_matches = len(dataset['Runs'])
average_runs = dataset['Runs'].mean()
position = dataset['Pos'].unique()

total_sizes = dataset.groupby('Opposition')['6s'].sum()

centuries = dataset.query("Runs >= 100")
innings = centuries["Inns"]
tons = centuries['Runs']


dataset['Pos'] = dataset['Pos'].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"
})

position_count = dataset["Pos"].value_counts()
position_values = position_count.values

print("Total number of runs: ", total_runs)
print("Total matches played: ", total_matches)
print("Average Runs: ", int(average_runs))
print("Positions played in: ", position)
print("Positions frequency: ", position_count)
print("Positions values: ", position_values)
print("Dataset: \n", dataset)
print("Runs: ", total_sizes)
print("Centuries Dataset \n", centuries)

ploting(dataset, "Pos")
ploting(dataset, 'Opposition')
ploting(dataset, 'Ground')
ploting(dataset, 'Dismissal')

runs_values = runs.values
runs_labels = runs.index
fig = plt.figure(figsize=(10,7))
plt.pie(runs_values, labels=runs_labels)
plt.show()

six_values =  total_sizes.values
six_labels =  total_sizes.index
fig = plt.figure(figsize=(10,7))
plt.pie( six_values, labels= six_labels)
plt.show()

fig = plt.figure(figsize=(10,7))
plt.bar(innings, tons, color='yellow', width=0.2)
plt.show()

fig = plt.figure(figsize=(10,7))
plt.bar(centuries['Opposition'], centuries["Runs"], color='yellow', width=0.2)
plt.show()