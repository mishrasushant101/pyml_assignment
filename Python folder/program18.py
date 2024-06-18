str1 = input("Enter the first string:")
str2 = input("Enter the second string:")
str1l = str1.lower()
str2l = str2.lower()
print("The strings are",str1l,"and",str2l)
if sorted(str1l) == sorted(str2l) :
    print("The words are anagrams of each other")
else:
    print("The words are not anagrams of eachother")
    