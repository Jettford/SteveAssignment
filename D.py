input_val = int(input("Please input a number?: "))

total = 0
while input_val > 0:
    total += input_val % 10
    input_val //= 10


print(total)