import requests
import webbrowser

def get_coordinates():
    place = input("Enter the location name: ")
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json", "limit": 5}   # <--- Number of results of place names

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    results = response.json()

    # Print the name and coordinates of each result
    for i, location in enumerate(results):
        lat = location["lat"]
        lon = location["lon"]
        name = location["display_name"]

        print(f"Result {i+1}: {name}")
        print(f"Latitude: {lat}, Longitude: {lon}")
        print()

        if i == 0:
            # Open Google Maps with the location in the default browser
            map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            webbrowser.open(map_url)

    # Return the latitude and longitude coordinates of the first result
    lat = results[0]["lat"]
    lon = results[0]["lon"]
    return (lat, lon)

# Call the function to get coordinates for the user-entered location
get_coordinates()
