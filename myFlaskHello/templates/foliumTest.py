import folium
import os
m = folium.Map(location=[29.488869,106.571034],
              zoom_start=14)

folium.Marker([29.488869,106.571034], popup='<i>Mt. Hood Meadows</i>').add_to(m)
m