from geopy.geocoders import Nominatim

class device :
    def get_address(latitude, longitude):
        address = Nominatim(user_agent="my_geocoder")
        location = address.reverse((latitude, longitude), exactly_one=True)
        return location.address if location else "Address not found"
    
    
    def information():
        city = input('enter your city name :')
        user = Nominatim(user_agent="my_geocoder")
        location = user.geocode(city)
        if location:
            print((location.latitude, location.longitude))
        else:
            print("Location not found") 