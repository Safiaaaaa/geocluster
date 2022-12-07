import json
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import numpy as np
import requests

import geojson
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
# from PIL import Image
from geocluster.registry import feat_labels, feat_dict
from geocluster.kmeans import cluster

n_clusters = st.slider('Number of clusters', 2, 20)
selection = st.multiselect('Features to cluster on',
     feat_labels, default=['Child poverty in % per planning area'])
if len(selection) == 0: 
    '''Choose the features you want to cluster on'''
    
# st.map(pd.DataFrame({'lat': [52.52437], 'lon': [13.41053]}), zoom=10)

# m = folium.Map(location=[52.52437, 13.41053], zoom_start=10)
# folium_static(m)

features_dict = feat_dict
features = []
for s in selection: 
    features.append(features_dict[s])

# API call
# url = 'http://127.0.0.1:8000/cluster'
# params={'n_clusters':n_cluster, 
#     'features': features
# }
# resp = requests.get(url=url, params=params).json()

# with open("/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/berlin_plr_num.geojson") as geo:
#     geo = geojson.load(geo)
geo = gpd.read_file('https://raw.githubusercontent.com/Safiaaaaa/geocluster/main/geocluster/data/plr_id.geojson')
df =  pd.read_csv('https://raw.githubusercontent.com/Safiaaaaa/geocluster/main/geocluster/data/full_dataset.csv')

clusters_df = cluster(df, n_clusters, features)

# feature = 'child_pov'
df['cluster'] = df['PLR_ID'].map(clusters_df['clusters'])

# colors = dict.fromkeys(np.arange(1, n_cluster+1), list(np.random.choice(range(256), size=3)))
# f'''{df['cluster']}'''

fig = px.choropleth_mapbox(data_frame = df,
        geojson=geo,
        locations="PLR_ID",
        featureidkey="properties.PLR_ID",
        color='cluster',
        # color_discrete_sequence=np.random.choice(range(256)),
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
        hover_name='PLR_ID',
        #hover_data={'PLR_ID':False,'child_pov':True}
        )

# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},) # coloraxis_colorbar= {'title':f"{shortname} in {unit}"}
st.plotly_chart(fig)
st.write("")

""" folium.Choropleth(
    geo_data='/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/berlin_plr.geojson',
    data= pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv'),
    columns=('PLR_ID', 'child_pov'),
    key_on= 'feature.properties.PLR_ID',
    fill_color='PuBu',
    bins=[0,20,50]
).add_to(m)
folium_static(m) """
"""

folium.GeoJson(
    json.loads(requests.get('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/berlin_plr.geojson').text),
    style_function=lambda feature: {
        'fillColor': linear(unemployment_dict[feature['id']]),
        'color': 'black',     #border color for the color fills
        'weight': 1,          #how thick the border has to be
        'dashArray': '5, 3'  #dashed lines length,space between them
    }
).add_to(m)
linear.add_to(usa_linear)   #adds colorscale or legend
"""
