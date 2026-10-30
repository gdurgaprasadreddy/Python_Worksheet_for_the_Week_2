numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num ** 2 for num in numbers]

print("Squares:", squares)
even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print("Even Numbers:")
print(even_numbers)
