import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('data.csv')
print(dataset.head(10))

total_runs = dataset['Runs'].sum()
total_matches = len(dataset['Runs'])
average_runs = dataset['Runs'].mean()
position = dataset['Pos'].unique()

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

fig = plt.figure(figsize=(10,7))
plt.show()

print("Total number of runs: ", total_runs)
print("Total matches played: ", total_matches)
print("Average Runs: ", int(average_runs))
print("Positions played in: ", position)
print("Positions frequency: ", position_count)
print(position_values)
print("Dataset: \n", dataset)