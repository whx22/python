# DRY principle : Don't Repeat Yourself

"""
define function
def function(paragram):
    statement
"""

def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"this sector area is {sector_area}")
    return sector_area

sector_area_1 = calculate_sector(160, 3)
sector_area_2 = calculate_sector(60, 15)
sector_area_3 = calculate_sector(30, 16)

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("three body".title())

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("beijing", "china"))
print(city_country("shanghai", "china"))
print(city_country("tokyo", "japan"))