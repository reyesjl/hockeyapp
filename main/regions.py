from math import sqrt

region_points = {
    'North East': (45.25, -73.15),      # Approximate center of northeastern United States and eastern Canada
    'South West': (32.75, -113.95),     # Approximate center of southwestern United States
    'West': (39.5, -116.5),             # Approximate center of western United States and western Canada
    'South East': (29.25, -82.5),       # Approximate center of southeastern United States
    'Midwest': (42.5, -91.5),           # Approximate center of midwestern United States
    'Eastern Canada': (45.5, -86.5),    # Approximate center of eastern Canada
    'Western Canada': (45.5, -126)      # Approximate center of western Canada
}

def nearest_region(latitude, longitude):
    min_distance = float('inf')
    nearest_region = None
    
    for region, (region_lat, region_lon) in region_points.items():
        distance = calculate_distance(latitude, longitude, region_lat, region_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_region = region
    
    return nearest_region


def calculate_distance(lat1, lon1, lat2, lon2):
    # Calculate the distance between two points using Euclidean distance
    lat_diff = lat2 - lat1
    lon_diff = lon2 - lon1
    return sqrt(lat_diff ** 2 + lon_diff ** 2)

