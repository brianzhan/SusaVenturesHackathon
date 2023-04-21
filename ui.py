import folium

# Define coordinates (latitude, longitude) for the center of the map and circle locations
map_center = (37.7749, -122.4194)
circle_locations = [
    (37.7749, -122.4194),  # San Francisco, CA
    (34.0522, -118.2437),  # Los Angeles, CA
    (40.7128, -74.0060),   # New York City, NY
    (41.8781, -87.6298),   # Chicago, IL
    (38.5816, -121.4944)   # Sacramento, CA
]

# Create a map centered on the US
us_map = folium.Map(location=map_center, zoom_start=4)

# Draw circles on the map
for location in circle_locations:
    folium.Circle(
        location=location,
        radius=50000,  # Circle radius in meters
        color="#007849",  # Circle color
        fill=True,
        fill_color="#007849",
        fill_opacity=0.5,
    ).add_to(us_map)

# Save the map to an HTML file
us_map.save("us_map_with_circles.html")