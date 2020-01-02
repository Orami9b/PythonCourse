import folium
map = folium.Map(location = (33.44, -112.07), tiles="Stamen Terrain")

featureGroup = folium.FeatureGroup(name = "My Map")
featureGroup.add_child(folium.Marker(location = (33.3, -112), popup = "Hello! I'm a pop up!", icon = folium.Icon(color = "green")))

map.add_child(featureGroup)

map.save("Map1.html")