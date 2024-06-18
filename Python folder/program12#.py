from datetime import datetime
current_year = datetime.now().year
birth_year = int(input("Enter your birthyear:"))
age = current_year - birth_year
print("Your age is:",age)