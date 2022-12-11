import streamlit as sts
import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import minmax_scale
from functions.registry import features_labels, features_dict
from functions.kmeans import cluster

# Loading data - berlin geojson and features dataframe

geo = gpd.read_file('https://raw.githubusercontent.com/Safiaaaaa/geocluster/main/geocluster/data/plr_id.geojson')
df =  pd.read_csv('https://raw.githubusercontent.com/Safiaaaaa/geocluster/main/geocluster/data/full_dataset.csv')

# Project introduction
st.title('Browse and cluster Berlin data')
st.write('For our final project of the data science bootcamp at le Wagon, in September 2022, we collected 105 features from Berlin Open Data Platform and OpenStreetMaps. With this webapp, we aim at making this data available - and visible. We are using KMeans Clustering to plot the distribution of individual ans multiple features.')

# Collect user input
n_clusters = st.slider('Number of clusters', 2, 20)
selection = st.multiselect('Features to cluster on',
     features_labels, default=['Child poverty in % per planning area'])
if len(selection) == 0: 
    st.header('Choose one or several features you want to cluster on')
else: 
    features = [features_dict[s] for s in selection]

    # API call
    # url = 'http://127.0.0.1:8000/cluster'
    # params={'n_clusters':n_cluster, 
    #     'features': features
    # }
    # resp = requests.get(url=url, params=params).json()

    # Compute clusters and add clusters columns to input df
    clusters_df = cluster(df, n_clusters, features)
    df['cluster'] = df['PLR_ID'].map(clusters_df['clusters']).astype(int).astype(str)

    # Customize displayed labels for map
    labels_dict = {'PLR_ID': False}
    for f in features: 
        labels_dict[f] = True

    # Create map
    fig = px.choropleth_mapbox(data_frame = df,
            geojson=geo,
            locations="PLR_ID",
            featureidkey="properties.PLR_ID",
            color='cluster',
            color_discrete_sequence= px.colors.qualitative.Alphabet,
            # color_discrete_map=colors,
            # color_continuous_scale="Viridis",
            # range_color=(df[features[selection[0]]].max(), df[features[selection[0]]].min()),
            mapbox_style="carto-positron",
            zoom=9,
            center={
                "lat": 52.52,
                "lon": 13.40
            },
            opacity=0.5,
            #labels= {f"{color}: {color} amount"},
            hover_name='PLR_NAME',
            hover_data=labels_dict
            )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
    # fig.update_traces(
    #     hovertemplate="<br>".join(key+f': {df[key]}' for key in labels_dict.keys())
    #     )
  
    st.plotly_chart(fig)

    # Build dataframe to display mean values of clusters
    with st.container():
        st.subheader("Mean values of selected features per cluster")
        cluster_centers = df.groupby('cluster').mean()[features]
        st.dataframe(cluster_centers, use_container_width=True)
        # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},) # coloraxis_colorbar= {'title':f"{shortname} in {unit}"}
