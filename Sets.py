
# 7 EASY EXAMPLES ON SETS IN PYTHON


# Example 1: Creating Sets
print("=" * 50)
print("Example 1: Creating Sets")
print("=" * 50)

# Creating a set with numbers
numbers = {1, 2, 3, 4, 5}
print("Numbers set:", numbers)

# Creating a set with strings
fruits = {"apple", "banana", "orange", "grape"}
print("Fruits set:", fruits)

# Creating an empty set (use set(), not {})
empty_set = set()
print("Empty set:", empty_set)
print()


# Example 2: Sets Automatically Remove Duplicates
print("=" * 50)
print("Example 2: Sets Automatically Remove Duplicates")
print("=" * 50)

# Notice how duplicates are automatically removed
numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5}
print("Set with duplicates:", numbers_with_duplicates)
print("Notice: duplicates are automatically removed!")
print()


# Example 3: Adding and Removing Elements
print("=" * 50)
print("Example 3: Adding and Removing Elements")
print("=" * 50)

colors = {"red", "blue", "green"}
print("Original set:", colors)

# Adding elements
colors.add("yellow")
colors.add("purple")
print("After adding:", colors)

# Removing elements
colors.remove("blue")  # Removes 'blue', error if not found
colors.discard("red")  # Removes 'red', no error if not found
print("After removing:", colors)
print()


# Example 4: Set Operations - Union and Intersection
print("=" * 50)
print("Example 4: Set Operations - Union and Intersection")
print("=" * 50)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union: combines all elements from both sets
union_result = set1.union(set2)
print("Union (all elements):", union_result)

# Intersection: common elements in both sets
intersection_result = set1.intersection(set2)
print("Intersection (common elements):", intersection_result)
print()


# Example 5: Checking if Element Exists in Set
print("=" * 50)
print("Example 5: Checking if Element Exists in Set")
print("=" * 50)

animals = {"dog", "cat", "bird", "fish"}
print("Animals set:", animals)

# Check if element exists
if "dog" in animals:
    print("Dog is in the set!")

if "lion" not in animals:
    print("Lion is not in the set!")

# Get set length
print(f"\nTotal animals: {len(animals)}")
print()




