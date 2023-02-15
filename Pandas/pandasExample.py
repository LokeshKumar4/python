import pandas as pd



df= pd.read_csv("pokemon.csv")
seriesType=df[1].squeeze()
seriesType.get([0,4,710],default=" hey")
