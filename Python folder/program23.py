cf = input("Type 'c' if you want answer in celcius or 'f' if you want answer in farenheit:")
inp = int(input("Enter the value to be converted:"))
if cf == 'f':
    fer = (9/5)*inp + 32
    print("The temp in farenheit is:",fer)
elif cf == 'c':
    cel = (inp-32)*5/9
    print("The temperature in celcius is:",cel)
else:
    print("Input error")