# Fizz Buzz program

# Get number of required integers
n = input("Enter the number of integers: ")
print(n)
n = int(n)

# For loop to calculate Fizz, Buzz and FizzBuzz
for i in range(n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    print(i)
