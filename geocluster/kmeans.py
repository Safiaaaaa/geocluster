from sklearn.cluster import KMeans
from sklearn.preprocessing import minmax_scale
import pandas as pd
import os

'''Function to compute kmeans clustering'''

def feature_df(df, features):
    features.append('PLR_ID')
    df = df[features]
    return df

def kmeans_clustering(n_clusters, df):
    db_scaled = minmax_scale(df)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit(db_scaled)
    df["clusters"] = clusters.labels_
    return df

if __name__ == "__main__":
    # df = pd.read_csv('/Users/Safia/code/Safiaaaaa/geo-clustering/geo-cluster/data/frontend_df.csv')
    print(pd.read_csv(os.path.join(os.path.dirname('__file__'),'geocluster', 'data', 'frontend_df.csv')))
    # print(kmeans_clustering(2,  feature_df(df, ['eating', 'culture', 'community'])))
    # features = ['eating', 'culture', 'community']
    # features.append('PLR_ID')
    # features.append('PLR_NAME')
    # print(features)
