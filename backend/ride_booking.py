import googlemaps
import urllib.parse

class RideBackend:
    def __init__(self, api_key):
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)

    def autocomplete_place(self, input_text):
        try:
            results = self.gmaps.places_autocomplete(input_text)
            return [r['description'] for r in results]
        except Exception as e:
            print(f"Autocomplete error: {e}")
            return []

    def get_coordinates(self, location_name):
        try:
            geocode_result = self.gmaps.geocode(location_name)
            if geocode_result:
                lat = geocode_result[0]['geometry']['location']['lat']
                lng = geocode_result[0]['geometry']['location']['lng']
                return lat, lng
        except Exception as e:
            print(f"Geocode error: {e}")
        return None, None

    def get_distance_km(self, origin, destination):
        try:
            result = self.gmaps.distance_matrix(origins=origin, destinations=destination, mode='driving')
            distance_text = result['rows'][0]['elements'][0]['distance']['text']
            distance_km = float(distance_text.replace(' km', '').replace(',', ''))
            return distance_km
        except Exception as e:
            print(f"Distance error: {e}")
            return 0.0

    def generate_static_map_url(self, pickup, dropoff, use_polyline=False):
        pickup_coords = self.get_coordinates(pickup)
        dropoff_coords = self.get_coordinates(dropoff)

        if not pickup_coords or not dropoff_coords:
            return None

        base_url = "https://maps.googleapis.com/maps/api/staticmap?"

        markers = [
            f"color:green|label:P|{pickup_coords[0]},{pickup_coords[1]}",
            f"color:red|label:D|{dropoff_coords[0]},{dropoff_coords[1]}"
        ]

        if use_polyline:
            try:
                directions = self.gmaps.directions(pickup, dropoff, mode="driving")
                if directions and directions[0].get("overview_polyline"):
                    encoded_polyline = directions[0]["overview_polyline"]["points"]
                    path = f"enc:{encoded_polyline}"
                else:
                    print("No polyline found, using straight path.")
                    path = f"color:0x0000ff|weight:5|{pickup_coords[0]},{pickup_coords[1]}|{dropoff_coords[0]},{dropoff_coords[1]}"
            except Exception as e:
                print(f"Polyline error: {e}")
                path = f"color:0x0000ff|weight:5|{pickup_coords[0]},{pickup_coords[1]}|{dropoff_coords[0]},{dropoff_coords[1]}"
        else:
            path = f"color:0x0000ff|weight:5|{pickup_coords[0]},{pickup_coords[1]}|{dropoff_coords[0]},{dropoff_coords[1]}"

        marker_params = "&".join([f"markers={urllib.parse.quote(m)}" for m in markers])
        path_param = f"path={urllib.parse.quote(path)}"
        size_param = "size=390x350"
        maptype_param = "maptype=roadmap"
        key_param = f"key={self.api_key}"

        return f"{base_url}{size_param}&{maptype_param}&{marker_params}&{path_param}&{key_param}"
