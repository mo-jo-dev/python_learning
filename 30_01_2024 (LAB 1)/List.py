# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
numbers = [1 , 2, 3, 4, 5]
print(numbers)                      # Print whole list
numbers.append(6)                   # Adding 6 in end
print(numbers)                      # Print whole list
print(numbers[0])                   # Print first element of array
print(numbers[1:3])                 # Print list from 1 to 3
print(numbers + [7, 8, 9, 10])      # Appending another list to numbers
print(numbers[-3:])                 # Slicing returns a new list
numbers[3] = 99                     # Replacing value at index 2
print(len(numbers))                 # Gives the length of String