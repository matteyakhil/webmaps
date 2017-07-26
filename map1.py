# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return "blue"
    elif 1000<= elevation < 3000:
        return "green"
    else:
        return "red"

map=folium.Map(location=[38,-98],zoom_start=5,tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")
fgp=folium.FeatureGroup(name="Population")
for coordinates in [[38.2,-99.15],[37.2,-97.02]]:
    fg.add_child(folium.Marker(location=coordinates,popup="This is a first market",icon=folium.Icon(color="Green")))
 

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el),icon=folium.Icon(color=color_producer(el))))
    """ 
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el),radius=6,fill_color=color.producer(el),color="grey",fill_opacity=0.7))

    """
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    
map.add_child(fg)
map.add_child(fgp)
    
map.add_child(folium.LayerControl(position='topright',collapsed=True,autoZIndex=True))

map.save("Map1.html")


