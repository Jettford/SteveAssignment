input_list = []

for i in range(3):
    input_value = int(input("What is your input number?: "))

    input_list.append(input_value)

print(f"The total is {sum(input_list)} and the average is {sum(input_list) / len(input_list)}")
