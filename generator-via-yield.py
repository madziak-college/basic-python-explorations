def generate_squares(numbers):
    for number in numbers:
        yield number**2

arr = [1, 2, 5]
generator = generate_squares(arr)
print(next(generator))
print(next(generator))
print(next(generator))