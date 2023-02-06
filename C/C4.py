input_list = []

input_val = 1 # :)
while input_val != 0:
    input_val = int(input("Please input a number?: "))

    input_list.append(input_val)

print(f"The total is {sum(input_list)} and the average is {sum(input_list) / len(input_list)}")


