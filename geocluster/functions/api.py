from fastapi import FastAPI, Query
from typing import Union, List
from fastapi.middleware.cors import CORSMiddleware
from geocluster.kmeans import feature_df, kmeans_clustering
import pandas as pd


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/cluster")
def cluster(n_clusters:int, features: Union[List[str], None] = Query(default='child_pov')):
    df = pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv')
    selected = feature_df(df, features)
    clusters_df = kmeans_clustering(n_clusters, selected)
    return clusters_df.to_dict()

if __name__ == "__main__":
    df = pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv')
    selected = feature_df(df, ['culture', 'community'])
    clusters = kmeans_clustering(2, selected)
    print(clusters.to_dict())
