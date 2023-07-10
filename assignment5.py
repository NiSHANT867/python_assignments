numbers = []
for i in range(5):
    num = float(input("Enter 5 numbers  : "))
    numbers.append(num)

#1) Calculate the sum of all the elements in the list
a = sum(numbers)
print("Sum of the numbers:", a)


#2) Find the smallest number
b = min(numbers)
print("Smallest number:", b)

#3) Find the largest number
c = max(numbers)
print("Largest number:", c)

#4) Display list in ascending order
d = sorted(numbers)
print("List in ascending order:", d)

#5) Display list in descending order
e = sorted(numbers, reverse=True)
print("List in descending order:", e)

#6) Convert list into tuple
f = tuple(numbers)
print("List converted into a tuple:", f)

#7) Delete the list
del numbers
print("List deleted.")
