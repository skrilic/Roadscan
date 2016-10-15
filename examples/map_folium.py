import folium
map_osm = folium.Map(location=[45.5236, 17.6750])
map_osm.save('osm.html')

# Popup samples https://github.com/python-visualization/folium
vis1 = [1, 2, 3]
vis2 = [1, 2, 3]
vis3 = [1, 2, 3]
buoy_map = folium.Map(location=[46.3014, -123.7390], zoom_start=7,
                      tiles='Stamen Terrain')
popup1 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(vis1, width=500, height=250))
folium.RegularPolygonMarker([47.3489, -124.708], fill_color='#43d9de', radius=12, popup=popup1).add_to(buoy_map)
popup2 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(vis2, width=500, height=250))
folium.RegularPolygonMarker([44.639, -124.5339], fill_color='#43d9de', radius=12, popup=popup2).add_to(buoy_map)
popup3 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(vis3, width=500, height=250))
folium.RegularPolygonMarker([46.216, -124.1280], fill_color='#43d9de', radius=12, popup=popup3).add_to(buoy_map)
buoy_map.save('NOAA_buoys.html')

# #JSON
# geo_path = r'data/antarctic_ice_edge.json'
# topo_path = r'data/antarctic_ice_shelf_topo.json'
#
# ice_map = folium.Map(location=[-59.1759, -11.6016],
#                    tiles='Mapbox Bright', zoom_start=2)
# ice_map.choropleth(geo_path=geo_path)
# ice_map.choropleth(geo_path=topo_path, topojson='objects.antarctic_ice_shelf')
# ice_map.save('ice_map.html')
