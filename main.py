import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import os

geocoder_key = "your key"

number = input("enter your number with country code :- ")

number = phonenumbers.parse(number)

location = geocoder.description_for_number(number, 'en')
service_provider = carrier.name_for_number(number, 'en')

geocoder = OpenCageGeocode(geocoder_key)
query = str(location)

result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print("lat - {lat} lng - {lng}" )

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat , lng], popup=location).add_to(myMap)


#html save
myMap.save("TargetLocation.html")
os.system("TargetLocation.html")

print(service_provider)

