"""
dictionary stores key-value pairs

dictionary = {key_1: value_1, key_2: value_2, ...}

mutable data type: list, dictionary
immutable data type: str, int, float, bool, tuple
"""

"""
tuple stores multiple values in a variable
tuple can be key of dictionary
list can be key of dictionary

example_tuple = (value_1, value_2, ...)
example_tuple.append(value) : Error
example_tuple.remove(value) : Error

example_list = [value_1, value_2, ...]
example_list.append(value) : Right
example_list.remove(value) : Right
"""

"""
dictionary usage

1. add & update key-value pair
dictionary[key] = value

2. judgement existence
key in dictionary return result(bool)

3. delete key-value pair
del dictionary[key]

4. calculate the number of key-value in dictionary
len(dictionary)
"""
friend = {"first_name": "Huxin", "last_name": "Wang", "age": 22, "city": "Wuhan"}
print("name: " + friend["last_name"] + friend["first_name"])
print("age: " + str(friend["age"]))
print("city: " + friend["city"])