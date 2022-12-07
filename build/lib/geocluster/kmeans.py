from sklearn.cluster import KMeans
from sklearn.preprocessing import minmax_scale
import pandas as pd
import os

'''Function to compute kmeans clustering'''

def feature_df(df, features):
    df_selected = df[features]
    df_scaled = pd.DataFrame(
        minmax_scale(df_selected), columns=features)
    df_scaled.index = df.PLR_ID
    return df_scaled

def kmeans_clustering(n_clusters, df):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit(df)
    df["clusters"] = clusters.labels_
    return df

def cluster(df, n_clusters:int, features=['child_pov']):
    # df = pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv')
    selected = feature_df(df, features)
    clusters_df = kmeans_clustering(n_clusters, selected)
    return clusters_df

if __name__ == "__main__":
    root_dir = os.path.dirname(__file__)
    csv_path = os.path.join(root_dir, "data", "df_dropna.csv")
    # df = pd.read_csv('/Users/Safia/code/Safiaaaaa/geo-clustering/geo-cluster/data/frontend_df.csv')
    # print(os.path.join(root_dir, csv_path))
    # print(feature_df(pd.read_csv(csv_path, ['child_pov'])))
    print(feature_df(pd.read_csv(os.path.join(root_dir,csv_path)), ['child_pov']))
    # print(kmeans_clustering(2, feature_df(pd.read_csv(os.path.join(os.path.dirname('__file__'),'geocluster', 'data', 'df_dropna.csv')), ['child_pov'])))
    # print(kmeans_clustering(2,  feature_df(df, ['eating', 'culture', 'community'])))
    # features = ['eating', 'culture', 'community']
    # features.append('PLR_ID')
    # features.append('PLR_NAME')
    # print(features)
