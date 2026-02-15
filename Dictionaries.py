
# 7 EASY EXAMPLES ON DICTIONARIES IN PYTHON


# Example 1: Creating a Simple Dictionary
print("=" * 50)
print("Example 1: Creating a Simple Dictionary")
print("=" * 50)

student = {
    "name": "Ahmed",
    "age": 20,
    "grade": "A"
}
print(student)
print()


# Example 2: Accessing Dictionary Values
print("=" * 50)
print("Example 2: Accessing Dictionary Values")
print("=" * 50)

person = {
    "name": "Fatima",
    "city": "Karachi",
    "age": 25
}

print("Name:", person["name"])
print("City:", person.get("city"))
print("Age:", person["age"])
print()


# Example 3: Adding and Updating Dictionary Items
print("=" * 50)
print("Example 3: Adding and Updating Dictionary Items")
print("=" * 50)

car = {
    "brand": "Toyota",
    "model": "Corolla"
}

print("Before update:", car)
car["year"] = 2023  # Adding new item
car["model"] = "Camry"  # Updating existing item
print("After update:", car)
print()


# Example 4: Removing Items from Dictionary
print("=" * 50)
print("Example 4: Removing Items from Dictionary")
print("=" * 50)

fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange"
}

print("Before removal:", fruits)
del fruits["grape"]  # Remove specific item
fruits.pop("orange")  # Remove using pop()
print("After removal:", fruits)
print()


# Example 5: Looping Through a Dictionary
print("=" * 50)
print("Example 5: Looping Through a Dictionary")
print("=" * 50)

colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}

print("Keys:")
for key in colors.keys():
    print(f"  {key}")

print("\nValues:")
for value in colors.values():
    print(f"  {value}")

print("\nKey-Value Pairs:")
for key, value in colors.items():
    print(f"  {key}: {value}")
print()


# Example 6: Dictionary with Different Data Types
print("=" * 50)
print("Example 6: Dictionary with Different Data Types")
print("=" * 50)

mixed_data = {
    "name": "Ali",           # String
    "age": 30,               # Integer
    "height": 5.9,           # Float
    "is_student": True,      # Boolean
    "subjects": ["Math", "Science", "English"],  # List
    "grades": {"Math": 85, "Science": 90}       # Nested Dictionary
}

print("Name:", mixed_data["name"])
print("Age:", mixed_data["age"])
print("Subjects:", mixed_data["subjects"])
print("Math Grade:", mixed_data["grades"]["Math"])
print()



# Example 7: Checking if Key Exists and Dictionary Length
print("=" * 50)
print("Example 7: Checking if Key Exists and Dictionary Length")
print("=" * 50)

phonebook = {
    "Ahmed": "0300-1234567",
    "Sara": "0301-2345678",
    "Hassan": "0302-3456789"
}

# Check if key exists
if "Ahmed" in phonebook:
    print("Ahmed's number:", phonebook["Ahmed"])

if "Ali" not in phonebook:
    print("Ali is not in the phonebook")

# Get dictionary length
print(f"\nTotal contacts: {len(phonebook)}")
print("All contacts:", list(phonebook.keys()))