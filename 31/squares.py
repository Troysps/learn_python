squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)

print(squares)

numbers=[]
for number in range(1,100):
    numbers.append(number**2)
print(numbers)

print(min(numbers))

print(max(numbers))

print(sum(numbers))

digits=[digit**2 for digit in range(0,99,3)]
print(digits) 
