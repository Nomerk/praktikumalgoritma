#NAMA ADITYA FAJRIAN ARYADEVA
#NIM 065002000315

import math

lat1 = float(input("Masukkan latitude titik pertama (dalam derajat): "))
lon1 = float(input("Masukkan longitude titik pertama (dalam derajat): "))
lat2 = float(input("Masukkan latitude titik kedua (dalam derajat): "))
lon2 = float(input("Masukkan longitude titik kedua (dalam derajat): "))

earth_radius = 6371.0

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

a = math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

jarak = earth_radius * c

print(f"Jarak antara dua titik adalah {jarak:.2f} kilometer.")
