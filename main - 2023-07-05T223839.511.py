from geopy.geocoders import Nominatim

def track_people(zip_codes):
    geolocator = Nominatim(user_agent="your_app_name")  # Replace "your_app_name" with your desired user agent

    for zip_code in zip_codes:
        location = geolocator.geocode(zip_code)
        if location is None:
            print(f"No location found for zip code: {zip_code}")
        else:
            latitude = location.latitude
            longitude = location.longitude
            print(f"Zip code: {zip_code} | Latitude: {latitude} | Longitude: {longitude}")

# Example usage
zip_codes = ["12345", "67890", "54321"]
track_people(zip_codes)
