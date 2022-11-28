import json
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import requests

# select_data = st.sidebar.radio("What data do you want to see?"
# ("Total_Pop", "Area_Region","Male_Pop",'Female_Pop'))

st.map(pd.DataFrame({'lat': [52.52437], 'lon': [13.41053]}), zoom_start=10)

m = folium.Map(location=[52.52437, 13.41053], zoom_start=10)
folium.Choropleth(
    geo_data='/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/berlin_plr.geojson',
    data= pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv'),
    columns=['PLR_ID', 'child_pov'],
    key_on= 'feature.properties.PLR_ID',
).add_to(m)
folium_static(m)


folium.GeoJson(
    json.loads(requests.get('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/berlin_plr.geojson').text),
    style_function=lambda feature: {
        'fillColor': linear(unemployment_dict[feature['id']]),
        'color': 'black',     #border color for the color fills
        'weight': 1,          #how thick the border has to be
        'dashArray': '5, 3'  #dashed lines length,space between them
    }
).add_to(usa_linear)
linear.add_to(usa_linear)   #adds colorscale or legend
