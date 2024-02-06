print("Enter the number: ")
num = int(input())
def isPalindrome(num):
    if(num == rev(num)):
        print("The number is a Palindrome")
    else:
        print("The number is not a Palindrome")

def rev(num):
    number = 0
    while num > 0:
        rem = num % 10
        number = number*10 + rem
        num = num // 10
    return number

isPalindrome(num)