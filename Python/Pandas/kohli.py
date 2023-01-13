import pandas as pd

dataset = pd.read_csv('data.csv')
new_dataset = dataset[['Runs', '4s', '6s', 'Opposition']]
vs_australia = dataset[dataset['Opposition'] == 'v Australia']
score_centuries = vs_australia[vs_australia['Runs'] >= 100]
total_runs = 0

print("First 10 rows \n", dataset.head(10))
print("Last 10 rows \n", dataset.tail(10))
print("Info \n", dataset.info())
print("Shape \n", dataset.shape)
print("Description \n", dataset.describe())
print("Opposition Collumn Description \n", dataset['Opposition'].describe())
print("Runs Value Count \n", dataset['Runs'].value_counts())

print(new_dataset)
print(new_dataset.describe())
print(new_dataset.iloc[2]['Runs'])

for run in vs_australia['Runs']:
    total_runs = total_runs + run

print(vs_australia)
print(total_runs)
print(vs_australia['Runs'].sum())
print(vs_australia['6s'].sum())

print(score_centuries)

def findCenturies(x):
    if(x>=100):
        return "OG"
    else:
        return "NOOB"

dataset['Centuries'] = dataset['Runs'].apply(findCenturies)
print(dataset)