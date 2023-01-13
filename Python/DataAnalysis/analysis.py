import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('data.csv')
print(dataset.head(10))

total_runs = dataset['Runs'].sum()
total_matches = len(dataset['Runs'])
average_runs = dataset['Runs'].mean()
position = dataset['Pos'].unique()


print("Total number of runs: ", total_runs)
print("Total matches played: ", total_matches)
print("Average Runs: ", int(average_runs))
print("Positions played in: ", position)