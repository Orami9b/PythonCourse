import folium
import pandas

def getColor(elevation):
   if row.ELEV > 3000:
      elevColor = "red"
   elif row.ELEV > 2000:
      elevColor = "orange"
   else:
      elevColor = "green"
   return elevColor

map = folium.Map(location = (33.44, -112.07), tiles="Stamen Terrain")

featureGroup = folium.FeatureGroup(name = "My Map")
volcanoList = pandas.read_csv("Volcanoes.txt")
html = """
Volcano name:<br><a href="https://www.google.com/search?q={name}+volcano" target="_blank">{name}</a><br>
Height: {elevation} m
"""

for index, row in volcanoList.iterrows():
   coordinates = (row.LAT, row.LON)
   iFrame = folium.IFrame(html.format(name = row.NAME, elevation = row.ELEV),
      width=200, height=100)
   featureGroup.add_child(folium.Marker(location = coordinates,
      popup = folium.Popup(iFrame, parse_html = True),
      icon = folium.Icon(color = getColor(row.ELEV))))

featureGroup.add_child(folium.GeoJson(data = open("world.json",
   encoding = "utf-8-sig").read(), style_function = 
      lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] > 25000000
      else "orange" if x["properties"]["POP2005"] > 10000000
      else "red"}))

map.add_child(featureGroup)
map.save("Map1.html")