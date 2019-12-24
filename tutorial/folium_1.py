import folium

wuhan_location = [30.546578, 114.283002]
dom_location = [30.529187, 114.358399]
txz_location = [30.661197, 114.378276]

m = folium.Map(
    location=wuhan_location,
    zoom_start=10,
    control_scale=True,
    tiles='Stamen Terrain'
)

tooltip = 'Click me!'

folium.Marker(dom_location, popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(m)
folium.Marker(txz_location, popup='<b>Timberline Lodge</b>', tooltip=tooltip).add_to(m)

m.save("../map_output/output.html")
