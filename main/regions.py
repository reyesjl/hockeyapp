import googlemaps
from decouple import config

def get_region(latitude, longitude):
    """
    Retrieves the administrative area level 1 (region) for a given latitude and longitude using the Google Maps Geocoding API.

    Parameters:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        api_key (str): Your Google Maps API key.

    Returns:
        str: The administrative area level 1 (region) name for the given latitude and longitude.
             If no region is found, returns 'All'.
    """
    # Retrieve Google Maps API key from environment variables
    google_maps_api_key = config('GOOGLE_MAPS_API_KEY')

    # Initialize Google Maps client with API key
    gmaps = googlemaps.Client(key=google_maps_api_key)
    
    # Reverse geocode the latitude and longitude to get address information
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    
    # Define a mapping of administrative area level 1 regions to major regions
    region_mapping = {
        # Major regions in the USA
        'Alabama': 'South',
        'Alaska': 'West',
        'Arizona': 'West',
        'Arkansas': 'South',
        'California': 'West',
        'Colorado': 'West',
        'Connecticut': 'North East',
        'Delaware': 'North East',
        'Florida': 'South',
        'Georgia': 'South',
        'Hawaii': 'West',
        'Idaho': 'West',
        'Illinois': 'Mid West',
        'Indiana': 'Mid West',
        'Iowa': 'Mid West',
        'Kansas': 'Mid West',
        'Kentucky': 'South',
        'Louisiana': 'South',
        'Maine': 'North East',
        'Maryland': 'North East',
        'Massachusetts': 'North East',
        'Michigan': 'Mid West',
        'Minnesota': 'Mid West',
        'Mississippi': 'South',
        'Missouri': 'Mid West',
        'Montana': 'West',
        'Nebraska': 'Mid West',
        'Nevada': 'West',
        'New Hampshire': 'North East',
        'New Jersey': 'North East',
        'New Mexico': 'West',
        'New York': 'North East',
        'North Carolina': 'South',
        'North Dakota': 'Mid West',
        'Ohio': 'Mid West',
        'Oklahoma': 'South',
        'Oregon': 'West',
        'Pennsylvania': 'North East',
        'Rhode Island': 'North East',
        'South Carolina': 'South',
        'South Dakota': 'Mid West',
        'Tennessee': 'South',
        'Texas': 'South',
        'Utah': 'West',
        'Vermont': 'North East',
        'Virginia': 'South',
        'Washington': 'West',
        'West Virginia': 'South',
        'Wisconsin': 'Mid West',
        'Wyoming': 'West',
        # Major regions in Canada
        'Alberta': 'Alberta',
        'British Columbia': 'British Columbia',
        'Manitoba': 'Manitoba',
        'New Brunswick': 'New Brunswick',
        'Newfoundland and Labrador': 'Newfoundland and Labrador',
        'Nova Scotia': 'Nova Scotia',
        'Ontario': 'Ontario',
        'Prince Edward Island': 'Prince Edward Island',
        'Quebec': 'Quebec',
        'Saskatchewan': 'Saskatchewan',
        'Northwest Territories': 'Northwest Territories',
        'Nunavut': 'Nunavut',
        'Yukon': 'Yukon'
    }
    
    # Iterate through the reverse geocode results to find the administrative area level 1 (region)
    for result in reverse_geocode_result:
        for component in result['address_components']:
            if 'administrative_area_level_1' in component['types']:
                region_name = component['long_name']
                print(region_name)
                # Check if the region name is in the mapping, if so, return the major region
                if region_name in region_mapping:
                    return region_mapping[region_name]
    
    # If no major region is found, return 'Unknown'
    return 'Unknown'

def get_coordinates(address):
    """
    Calls the Google Maps Geocoding API to get latitude and longitude for the given address.

    Args:
        address: The physical address entered by the user.

    Returns:
        A dictionary containing the latitude and longitude coordinates.
    """
    # Retrieve Google Maps API key from environment variables
    google_maps_api_key = config('GOOGLE_MAPS_API_KEY')

    # Initialize Google Maps client with API key
    gmaps = googlemaps.Client(key=google_maps_api_key)

    try:
        # Perform geocoding request
        geocode_result = gmaps.geocode(address)

        if geocode_result:
            # Extract latitude and longitude from the first result
            location = geocode_result[0]['geometry']['location']
            print("Response from geocoding: " + str(location['lat']) + str(location['lng']))
            return {'lat': location['lat'], 'lng': location['lng']}
        else:
            # Handle empty response
            print("Empty response from geocoding service")
            return {'lat': 0.0, 'lng': 0.0}
    except googlemaps.exceptions.ApiError as e:
        # Handle API errors
        print(f"Error retrieving coordinates: {e}")
        return {'lat': 0.0, 'lng': 0.0}

