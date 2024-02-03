# Write a Python program that takes the input from the user and prints the subject and marks from a dictionary. 
# Take five different subjects of your choice.

student_database = {'abhay': {'English':99, 'Hindi':67,'Maths':99,'Science':89,'Social Science':42},
                    'abhijit':{'English':78, 'Hindi':99,'Maths':99,'Science':77,'Social Science':45},
                    'harishankar':{'English':58, 'Hindi':97,'Maths':99,'Science':64,'Social Science':62},
                    'mohit': {'English':78,'Hindi':66,'Maths':56,'Science':98,'Social Science': 100}}

print("Enter the Student whose marks you want: ")
s_name = input()
count = 0
for i in student_database:
    if student_database[s_name]:
        print(student_database[s_name])
        break
    # else:
        # count = count + 1

# if count == i:
#     print("No stdent Found with that name!!")