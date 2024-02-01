"""
dictionary function
dictionary.keys() # return all keys
dictionary.values() # return all values
dictionary.items() # return all key-value pairs
"""

temperature_dict = {"111": 37.2, "112": 36.5, "113": 36.8, "114": 37.0, "115": 36.9}
for starr_id, temperature in temperature_dict.items():
    if temperature >= 37:
        print(starr_id)

for temperature_tuple in temperature_dict.items():
    starr_id = temperature_tuple[0]
    temperature = temperature_tuple[1]
    if temperature >= 37:
        print(starr_id)

rivers = {"Nile": "Egypt", "Yangtze River": "China", \
          "Amazon River": "Brazil"}
for river, country in rivers.items():
    print("The " + river + " run through " + country + ".")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)