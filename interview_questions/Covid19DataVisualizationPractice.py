import pandas
data = pandas.read_csv("https://storage.googleapis.com/covid19-open-data/v3/epidemiology.csv")
print(data.describe())