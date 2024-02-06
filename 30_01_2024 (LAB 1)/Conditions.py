# condition
print("Enter your Gender: ")
gender = input()
print("Enter your current age: ")
age = int(input())
if gender == "MALE" or gender == "Male" or gender == "male":
    if age > 21:
        print("Hooray!! You can marry")
    else:
        print("Sorry!! You can't marry")
else:    
    if age > 18:
        print("Hooray!! You can marry")
    else:
        print("Sorry!! You can't marry")
