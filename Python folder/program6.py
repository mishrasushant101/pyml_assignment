filename = input("Enter the name of the file: ")

try:
     with open(filename, "r") as file:
        content = file.read()
        print("Content of", filename + ":")
        print(content)
except FileNotFoundError:
        print("File not found. Please make sure the file exists and try again.")