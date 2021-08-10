
import pandas as pd
from datetime import datetime
import folium
import geojson

#Import Data
path_to_json = 'assets/data/london_postcodes.json'
path_to_json_2 = 'assets/data/ulez_2021.geojson'
path = 'assets/data/postcode_rent_data.csv'
with open(path_to_json) as f:
    gj = geojson.load(f)
with open(path_to_json_2) as f:
    gj_2 = geojson.load(f)
df1 = pd.read_csv(path)
#Import Data end 

#Edit geoJSON for data on hover
tooltip_text = { x: y for x, y in zip(df1['Postcode'], df1['Average rent per month'])}
for idx,x in enumerate(gj['features']):
    this_tooltip_text = tooltip_text[x['properties']['Name']]
    gj['features'][idx]['properties']['Average rent per month (£)'] = this_tooltip_text
gj_data = gj.copy()
#Edit geoJSON for data on hover end

#Generate folium map
frame = folium.Figure(width=900, height=500)
fig = folium.Map(
    location=[51.5, -0.1],
    tiles="cartodbpositron",
    zoom_start=10.2).add_to(frame)
folium.Choropleth(
    geo_data=gj,
    data= df1,
    columns=["Postcode", "Average rent per month"],
    fill_color= "BuPu",
    fill_opacity=1,
    line_opacity=0.5,
    key_on ="feature.properties.Name",
    legend_name= "Average rent per month (£)",
    name="choropleth",
    highlight = True
).add_to(fig)
folium.GeoJson(
    gj_2,
    name="London Ultra Low Emission Zone",
    style_function=lambda feature: {
        "fillColor": 'Red',
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.5,
    },
).add_to(fig)
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.5, 
                                'weight': 0.1}
data_on_hover = folium.features.GeoJson(data = gj_data, style_function=style_function, control=False, highlight_function=highlight_function, tooltip=folium.features.GeoJsonTooltip(
    fields=['Name', 'Average rent per month (£)'],
    aliases=['Postcode: ', 'Average rent per month (£): '],
    style=("background-color: white; color: #333333; font-family: arial; font-size: 14px; padding: 10px;")))
folium.Marker(
    location=[51.50123, -0.018097],
    popup="Canary Wharf",
    icon=folium.Icon(color="red", icon="dot-circle-o", prefix='fa'),
).add_to(fig)
folium.Marker(
    location=[51.51333, -0.088947],
    popup="City of London",
    icon=folium.Icon(color="red", icon="dot-circle-o", prefix='fa'),
).add_to(fig)
folium.Marker(
    location=[51.529782, -0.024967],
    icon=folium.Icon(color="green", icon="fa-building-o", prefix='fa'),
).add_to(fig)
folium.Marker(
    location=[51.519674, -0.059866],
    icon=folium.Icon(color="purple", icon="fa-building-o", prefix='fa'),
).add_to(fig)
folium.Marker(
    location=[51.51006, -0.02001],
    icon=folium.Icon(color="purple", icon="fa-building-o", prefix='fa'),
).add_to(fig)
folium.Marker(
    location=[51.507644, -0.061251],
    icon=folium.Icon(color="purple", icon="fa-building-o", prefix='fa'),
).add_to(fig)
folium.Marker(
    location=[51.530257, -0.060310],
    icon=folium.Icon(color="purple", icon="fa-building-o", prefix='fa'),
).add_to(fig)
folium.Marker(
    location=[51.543211, -0.042667],
    icon=folium.Icon(color="purple", icon="fa-building-o", prefix='fa'),
).add_to(fig)
fig.add_child(data_on_hover)
fig.keep_in_front(data_on_hover)
folium.LayerControl().add_to(fig)
#Generate folium map end 

#Save folium map to html
fig.save("assets/folium/folium_obj.html", "w")
#Save folium map to html end

# Grab timestamp
data_updated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Write out to file (.html)
html_str = (
    '<p><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zm.5 4.75a.75.75 0 00-1.5 0v3.5a.75.75 0 00.471.696l2.5 1a.75.75 0 00.557-1.392L8.5 7.742V4.75z"></path></svg> Latest Data: '
    + data_updated
    + "</p>"
)
with open("_includes/update.html", "w") as file:
    file.write(html_str)