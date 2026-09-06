roll_number = {1: "Alice", 2: "Bob", 3: "Charlie", 4: "David", 5: "Eve"}
print(roll_number[1])  # Output: Alice
print(roll_number.get(2))  # Output: Bob
roll_number[6] = "Frank"  # Adding a new key-value pair
print(roll_number.get(3, "Not Found"))  # Output: Not Found
print(roll_number.keys())  # Output: dict_keys([1, 2, 3, 4, 5, 6])
print(roll_number.values())  # Output: dict_keys([1, 2, 3, 4, 5, 6])
print(roll_number.keys(), roll_number.values())  # Output: dict_values(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'])