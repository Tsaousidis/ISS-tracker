
import requests
import folium
import time
import webbrowser

def get_iss_position():
    """Fetch the current position of the ISS."""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    return latitude, longitude

def update_iss_map():
    """Continuously update the ISS map in real-time."""
    webbrowser.open("iss_map.html")  # Open the map in a browser
    try:
        while True:
            lat, lon = get_iss_position()
            
            # Create a new map centered on the updated ISS position
            iss_map = folium.Map(location=[lat, lon], zoom_start=3)
            folium.Marker(
                location=[lat, lon],
                popup=f"ISS Location\nLatitude: {lat},\nLongitude: {lon}",
                icon=folium.Icon(color="red", icon="cloud")
            ).add_to(iss_map)

            # Save and overwrite the map file
            iss_map.save("iss_map.html")
            print(f"ISS Updated: Lat={lat}, Lon={lon}")

            # Wait for 10 seconds before updating again
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nStopping ISS tracker.")

if __name__ == "__main__":
    update_iss_map()
