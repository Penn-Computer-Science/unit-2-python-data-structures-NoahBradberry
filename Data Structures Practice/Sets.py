my_set = {"Apple", "Banana", "Watermelon", "Mango", "Peach", "Blueberry"}
my_set.add("Kiwi")
my_set.remove("Mango")
other_set ={"Mango", "Pineapple", "Strawberry", "Watermelon", "Blueberry", "Orange"}
print("Fruits you both like " + str(my_set.intersection(other_set)))
print("Fruits only you like " + str(my_set.difference(other_set)))
print("All fruits either of you like " + str(my_set.union(other_set)))