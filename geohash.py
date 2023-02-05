import pandas as pd
import geohash2

df = pd.read_csv("Austin_Police_Stations.csv")
df = df.reset_index()

geohash = []
for index in df.index:
    geohash.append(geohash2.encode(df['x'][index], df['y'][index]))
df['geohash'] = geohash
df.to_csv("out.csv", index=False)
