import pandas as pd


data = pd.read_csv("Digital service prices, June 2020 - Raw Data.csv")
data.groupby(by="Service").count().sort_values(by="Country", ascending=False)
netflix_data = data.loc[data["Service"] == "Netflix"].copy()
netflix_data.to_csv("../netflix_data.csv")
