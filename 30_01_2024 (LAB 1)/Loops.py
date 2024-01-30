# Loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Enter the number whose table you want: ")
num = int(input())
for i in numbers:
    print(num, "x", i, "=", num*i)