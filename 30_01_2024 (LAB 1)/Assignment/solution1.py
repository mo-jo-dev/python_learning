# Q-> Write a Python program to reverse a string and check if it is a palindrome or not.
print("Enter a string: ")
string = input()
temp = string
ans = ""
while len(string) != 0:
    ans = ans + string[-1]
    string = string[:-1]

def check_palin_string(string, ans):
    return ans == string

if(check_palin_string(temp, ans)):
    print("Palindrome")
else:
    print("Not a Palindrome")
