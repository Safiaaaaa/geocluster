import json
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import requests

import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gdp
import plotly.express as px
from PIL import Image

"""values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
"""
select_data = st.slider('Number of clusters', 1, 20)

# st.map(pd.DataFrame({'lat': [52.52437], 'lon': [13.41053]}), zoom=10)

# m = folium.Map(location=[52.52437, 13.41053], zoom_start=10)
# folium_static(m)

with open("/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/berlin_plr.geojson") as response:
    geo = json.load(response)

fig = px.choropleth_mapbox(data_frame = pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv'),
        geojson=geo,
        locations="PLR_ID",
        color='child_pov',
        color_continuous_scale="Viridis",
        mapbox_style="open-street-map",
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
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},) # coloraxis_colorbar= {'title':f"{shortname} in {unit}"}
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
