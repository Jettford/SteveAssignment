input_value = int(input("What is your input number?: "))

print(sum([pow(item, 2) for item in list(range(1, input_value + 1))]))