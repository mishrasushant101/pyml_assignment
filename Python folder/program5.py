user_input = input("Enter a string: ")

with open("output.txt", "w") as file:
    file.write(user_input)

print("String has been written to output.txt")

