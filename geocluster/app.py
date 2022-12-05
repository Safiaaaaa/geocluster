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
# from PIL import Image


select_data = st.slider('Number of clusters', 1, 20)
selection = st.multiselect('Features to cluster on',
     ('Child poverty in % per planning area',
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
 'Population with not identified origin in % per planning area'), default=['Child poverty in % per planning area'])

# st.map(pd.DataFrame({'lat': [52.52437], 'lon': [13.41053]}), zoom=10)

# m = folium.Map(location=[52.52437, 13.41053], zoom_start=10)
# folium_static(m)

features = {'Population with migration background in % per planning area': 'mig_rate',
 'Unemployment in % per planning area': 'unemployme',
 'Welfare beneficiaries in % per planning area': 'welfare',
 'Child poverty in % per planning area': 'child_pov',
 'Dynamic of unemployment in % (2018 to 2020) per planning area': 'dyn_unempl',
 'Dynamic of welfare in % (2018 to 2020) per planning area': 'dyc_welfare',
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
 'Vegetation volume in m3/m2 per planning area': 'vgpm20',
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

with open("/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/berlin_plr_num.geojson") as response:
    geo = json.load(response)
df =  pd.read_csv('/Users/Safia/code/Safiaaaaa/geocluster/geocluster/data/df_dropna.csv')
# feature = 'child_pov'
fig = px.choropleth_mapbox(data_frame = df,
        geojson=geo,
        locations="PLR_ID",
        featureidkey="properties.PLR_ID",
        color=features[selection[0]],
        color_continuous_scale="Viridis",
        range_color=(df[features[selection[0]]].max(), df[features[selection[0]]].min()),
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
