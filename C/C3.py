input_list = []

i = 0
while i != 5:
    i += 1

    input_list.append(int(input("Please input a number?: ")))

print(f"The total is {sum(input_list)} and the average is {sum(input_list) / len(input_list)}")


