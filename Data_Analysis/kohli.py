import pandas as pd
df = pd.read_csv("dataset.csv")

#print(df.tail(10))

#print(df.info())
#print(df.shape)

# print(df.describe())

# print(df["Runs"].value_counts)

# new_df = df[["Runs", " 4s"," 6s"]]
# print(new_df)
# print(new_df.iloc[2]["Runs"])

#vs_aussies = df[df[" Opposition    "] == " v Australia   "]
# print(vs_aussies)
# total_runs = 0
# for i in vs_aussies["Runs"]:
#     total_runs = total_runs+i
# print(total_runs)    
#print(vs_aussies[vs_aussies["Runs"]>=100])

def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"] = df["Runs"].apply(find_centuries)    
print(df)        