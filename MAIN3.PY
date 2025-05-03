# Creating an object with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Creating an array
fruits = ["apple", "banana", "cherry", "date"]

# Displaying values from the object using keys
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Displaying values from the array using index
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Using join to display the whole array as a string
print("Fruits (joined):", ", ".join(fruits))

# Using pop to remove and display the last element of the array
last_fruit = fruits.pop()
print("Popped fruit:", last_fruit)

# Displaying the array after using pop
print("Fruits after pop:", fruits)