my_dictionary = {"United States" : "Washington D.C.", "Japan": "Tokyo", "United Kingdom":"London", "South Africa" : "Cape Town", "Mexico": "Mexico City" }
print(my_dictionary["Japan"])
print(my_dictionary["Mexico"])
my_dictionary["France"] = "Paris"
my_dictionary["United States"] = "Indianapolis"

for l in my_dictionary:
    print(l)
    print(my_dictionary[l])