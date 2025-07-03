import googlemaps
import urllib.parse
import random
import string

class RideBackend:
    '''
    A class to interact with Google Maps API and Booking Page/s for ride booking functionalities.
    '''
    def __init__(self, api_key):
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)

        # Fixed driver and vehicle info
        self.driver_data = {
            "Motorcycle": {
                "img": "moto_rider.png",
                "driver_name": "Princess Marian",
                "vehicle_name": "Suzuki XR",
                "license_plate": "ABC-123"
            },
            "4-seater": {
                "img": "4seater_driver.png",
                "driver_name": "Mary Baruruth",
                "vehicle_name": "Honda Civic",
                "license_plate": "XYZ-456"
            },
            "6-seater": {
                "img": "6seater_driver.png",
                "driver_name": "Maryjoy Caranters",
                "vehicle_name": "Toyota 2022",
                "license_plate": "DEF-789"
            }
        }
    
    # Calculate fare based on distance and vehicle type
    def calculate_fare(self, distance_km, vehicle_type):
        # Base prices
        base_fares = {
            "Motorcycle": 50,
            "4-seater": 120,
            "6-seater": 150
        }

        base_fare = base_fares.get(vehicle_type, 50)  # Default to 50 if unknown

        if distance_km <= 2:
            return base_fare
        elif distance_km <= 7:
            return base_fare + (distance_km - 2) * 10
        else:
            return base_fare + (5 * 10) + (distance_km - 7) * 15

    # Autocomplete place suggestions
    def autocomplete_place(self, input_text):
        try:
            results = self.gmaps.places_autocomplete(input_text)
            return [r['description'] for r in results]
        except Exception as e:
            print(f"Autocomplete error: {e}")
            return []

    # Get coordinates (lat, lng) from place name
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

    # Calculate driving distance in kilometers
    def get_distance_km(self, origin, destination):
        try:
            result = self.gmaps.distance_matrix(origins=origin, destinations=destination, mode='driving')
            distance_text = result['rows'][0]['elements'][0]['distance']['text']
            distance_km = float(distance_text.replace(' km', '').replace(',', ''))
            return distance_km
        except Exception as e:
            print(f"Distance error: {e}")
            return 0.0

    # Generate static map URL with or without polyline
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
        size_param = "size=390x405"
        maptype_param = "maptype=roadmap"
        key_param = f"key={self.api_key}"

        return f"{base_url}{size_param}&{maptype_param}&{marker_params}&{path_param}&{key_param}"

    # Generate random Booking ID (e.g., "8AF5T1XQ")
    def generate_booking_id(self, length=8):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    # Get estimated driving duration (e.g., "12 mins")
    def get_estimated_duration(self, origin, destination):
        try:
            result = self.gmaps.distance_matrix(origins=origin, destinations=destination, mode='driving')
            duration_text = result['rows'][0]['elements'][0]['duration']['text']
            return duration_text
        except Exception as e:
            print(f"Duration error: {e}")
            return "--"

    # Get driver and vehicle info by type
    def get_driver_info(self, vehicle_type):
        return self.driver_data.get(vehicle_type, {
            "driver_name": "--",
            "vehicle_name": "--",
            "license_plate": "--"
        })
