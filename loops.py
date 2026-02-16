# Example 1: Basic for loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# Example 2: While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Example 3: For loop with range
for i in range(10):
    if i % 2 == 0:
        print(i)

# Example 4: Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# Example 5: Loop with break
for x in range(1, 20):
    if x > 10:
        break
    print(x)

# Example 6: Loop through string
text = "hello"
for char in text:
    print(char.upper())

# Example 6: Loop through string
text = "hello"
for char in text:
    print(char.upper())

# Example 7: Loop with continue
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)

# Example 8: Sum numbers in a loop
total = 0
for n in [10, 20, 30, 40]:
    total += n
print(total)

# Example 9: Loop backwards
for i in range(5, 0, -1):
    print(i)