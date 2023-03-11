import requests
import webbrowser
import tkinter as tk

def get_coordinates():
    place = entry.get()
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json", "limit": 10}   # <--- Number of results of place names

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    results = response.json()

    # Create a new window to display the results
    result_window = tk.Toplevel(root)

    # Print the name and coordinates of each result
    for i, location in enumerate(results):
        lat = location["lat"]
        lon = location["lon"]
        name = location["display_name"]

        label = tk.Label(result_window, text=f"Result {i+1}: {name}")
        label.pack()
        label = tk.Label(result_window, text=f"Latitude: {lat}, Longitude: {lon}")
        label.pack()
        label = tk.Label(result_window, text="")
        label.pack()

        if i == 0:
            # Open Google Maps with the location in the default browser
            map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            webbrowser.open(map_url)

    # Return the latitude and longitude coordinates of the first result
    lat = results[0]["lat"]
    lon = results[0]["lon"]
    return (lat, lon)


# Create the main window
root = tk.Tk()
root.title("Get Coordinates")

# Create the text box and button
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10)

button = tk.Button(root, text="Get Coordinates", command=get_coordinates)
button.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
