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
# from geocluster.registry import feat_labels, feat_dict
# from geocluster.kmeans import cluster

# Loading data - berlin geojson and features dataframe

geo = gpd.read_file('https://raw.githubusercontent.com/Safiaaaaa/geocluster/main/geocluster/data/plr_id.geojson')
df =  pd.read_csv('https://raw.githubusercontent.com/Safiaaaaa/geocluster/main/geocluster/data/full_dataset.csv')

def feature_df(df, features):
    df_selected = df[features]
    df_scaled = pd.DataFrame(
        minmax_scale(df_selected), columns=features)
    df_scaled['PLR_NAME'] = df.PLR_NAME
    df_scaled.index = df.PLR_ID
    return df_scaled

def kmeans_clustering(n_clusters, df):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit(df.drop(columns='PLR_NAME'))
    df["clusters"] = clusters.labels_
    return df

def cluster(df, n_clusters, features=['child_pov']):
    # df = pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv')
    selected = feature_df(df, features)
    clusters_df = kmeans_clustering(n_clusters, selected)
    return clusters_df

feat_labels = ['Child poverty in % per planning area',
 'Unemployment in % per planning area',
 'Welfare beneficiaries in % per planning area',
 'Population with migration background in % per planning area',
 'Dynamic of unemployment in % (2018 to 2020) per planning area',
 'Dynamic of welfare in % (2018 to 2020) per planning area',
 'Dynamic of child poverty in % (2018 to 2020) per planning area',
 'Average advertised rent in €/m2 per planning area',
 'Social housing in % per planning area',
 'Share of municipal housing companies in the housing stock in % per planning area',
 'Conversion of multi-family houses into condos in % per planning area',
 'Dynamic of condo conversion in % (2015 to 2020) per planning area',
 'Aparments sale in % per planning area',
 'Dynamic of apartment sales in % (2015 to 2020) per planning area',
 'Share of inhabitants with at least 5 years of residence in % per planning area',
 'Amount of public transport stops within 500 m, incl. bus per planning area',
 'Amount of restaurants and cafés within 500 m (exc. fast food) per planning area',
 'Amount of cultural institutions within 500 m (museums, cinemas, theaters, etc.) per planning area',
 "Amount of extra-curriculum educational institutions within 500 m (music and language schools) per planning area",
 'Amount of urban furniture (picnic tables, benches, bbq, water points, etc.) within 500 m per planning area',
 'Amount of places for outdoor leisure (swimming pools, parks, playgrounds, etc.) within 500 m per planning area',
 'Amount of bars, pubs, nightclubs, etc. within 500 m per planning area',
 'Share of houses built before 1940 in % (as of 2015) per planning area',
 'Share of houses built between 1941 and 1991 in % (as of 2015) per planning area',
 'Share of houses built between 1991 and 2001 in % (as of 2015) per planning area',
 'Vegetation volume in m3/m2 per planning area',
 'Amount of other types of schools per planning area',
 'Amount of vocational schools per planning area',
 'Amount of primary schools per planning area',
 'Amount of Gymnasiums per planning area',
 'Amount of other secondary schools per planning area',
 'Amount of private schools per planning area',
 'Amount of schools for children with special needs per planning area',
 'Amount of kindergartens per planning area',
 'Amount of rail / U-bahn / S-bahn and tram stations per planning area',
 'Population with EU15-origin in % per planning area', 'Population with EU28-origin in % per planning area',
 'Population with Poland-origin in % per planning area', 'Population with Ex-Yugoslavia-origin in % per planning area',
 'Population with Post-Soviet states-origin in % per planning area', 'Population with Turkey origin in % per planning area',
 'Population with Arab-origin in % per planning area', 'Population with Other-origin in % per planning area',
 'Population with not identified origin in % per planning area']

feat_dict = {'Population with migration background in % per planning area': 'mig_rate',
 'Unemployment in % per planning area': 'unemployme',
 'Welfare beneficiaries in % per planning area': 'welfare',
 'Child poverty in % per planning area': 'child_pov',
 'Dynamic of unemployment in % (2018 to 2020) per planning area': 'dyn_unempl',
 'Dynamic of welfare in % (2018 to 2020) per planning area': 'dyn_welfar',
 'Dynamic of child poverty in % (2018 to 2020) per planning area': 'dyn_child',
 'Average advertised rent in €/m2 per planning area': 'ave_rent',
 'Social housing in % per planning area': 'social_hou',
 'Share of municipal housing companies in the housing stock in % per planning area': 'public_hou',
 'Conversion of multi-family houses into condos in % per planning area': 'rent_to_pr',
 'Dynamic of condo conversion in % (2015 to 2020) per planning area': 'dyn_r_to_p',
 'Aparments sale in % per planning area': 'sales',
 'Dynamic of apartment sales in % (2015 to 2020) per planning area': 'dyn_sales',
 'Share of inhabitants with at least 5 years of residence in % per planning area': 'five_y_pls',
 'Amount of public transport stops within 500 m, incl. bus per planning area': 'public_tra',
 'Amount of restaurants and cafés within 500 m (exc. fast food) per planning area': 'eating',
 'Amount of cultural institutions within 500 m (museums, cinemas, theaters, etc.) per planning area': 'culture',
 "Amount of extra-curriculum educational institutions within 500 m (music and language schools)' per planning area": 'education',
 'Amount of urban furniture (picnic tables, benches, bbq, water points, etc.) within 500 m per planning area': 'outdoor_fa',
 'Amount of places for outdoor leisure (swimming pools, parks, playgrounds, etc.) within 500 m per planning area': 'outdoor_le',
 'Amount of bars, pubs, nightclubs, etc. within 500 m per planning area': 'night_life',
 'Share of houses built before 1940 in % (as of 2015) per planning area': 'B_1940',
 'Share of houses built between 1941 and 1991 in % (as of 2015) per planning area': 'B_1941_199',
 'Share of houses built between 1991 and 2001 in % (as of 2015) per planning area': 'B_1991_201',
 'Vegetation volume in m3/m2 per planning area': 'vegpm20',
 'Amount of other types of schools per planning area': 'other_sch',
 'Amount of vocational schools per planning area': 'vocat_sch',
 'Amount of primary schools per planning area': 'primary_sc',
 'Amount of Gymnasiums per planning area': 'Gymnasium',
 'Amount of other secondary schools per planning area': 'secon_sch',
 'Amount of private schools per planning area': 'priv_schoo',
 'Amount of schools for children with special needs per planning area': 'sp_nee_sch',
 'Amount of kindergartens per planning area': 'kita',
 'Amount of rail / U-bahn / S-bahn and tram stations per planning area': 'stations',
 'Population with EU15-origin in % per planning area': 'HK_EU15',
 'Population with EU28-origin in % per planning area': 'HK_EU28',
 'Population with Poland-origin in % per planning area': 'HK_Polen',
 'Population with Ex-Yugoslavia-origin in % per planning area': 'HK_EheJug',
 'Population with Post-Soviet states-origin in % per planning area': 'HK_EheSU',
 'Population with Turkey origin in % per planning area': 'HK_Turk',
 'Population with Arab-origin in % per planning area': 'HK_Arab',
 'Population with Other-origin in % per planning area': 'HK_Sonst',
 'Population with not identified origin in % per planning area': 'HK_NZOrd'}

# Project introduction
st.title('Browse and cluster Berlin data')
st.write('For our final project of the data science bootcamp at le Wagon, in September 2022, we collected 105 features from Berlin Open Data Platform and OpenStreetMaps. With this webapp, we aim at making this data available - and visible. We are using KMeans Clustering to plot the distribution of individual ans multiple features.')

# Collect user input
n_clusters = st.slider('Number of clusters', 2, 20)
selection = st.multiselect('Features to cluster on',
     feat_labels, default=['Child poverty in % per planning area'])
if len(selection) == 0: 
    st.header('Choose one or several features you want to cluster on')
else: 
        
    features_dict = feat_dict
    features = [features_dict[s] for s in selection]

    # API call

    # url = 'http://127.0.0.1:8000/cluster'
    # params={'n_clusters':n_cluster, 
    #     'features': features
    # }
    # resp = requests.get(url=url, params=params).json()

    clusters_df = cluster(df, n_clusters, features)

    # feature = 'child_pov'
    df['cluster'] = df['PLR_ID'].map(clusters_df['clusters']).astype(int).astype(str)

    # colors = dict.fromkeys(np.arange(1, n_cluster+1), list(np.random.choice(range(256), size=3)))
    # f'''{df['cluster']}'''
    labels_dict = {'PLR_ID': False}
    for f in features: 
        labels_dict[f] = True

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

    with st.container():
        st.subheader("Mean values of selected features per cluster")
        cluster_centers = df.groupby('cluster').mean()[features]
        st.dataframe(cluster_centers, use_container_width=True)
        # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},) # coloraxis_colorbar= {'title':f"{shortname} in {unit}"}
