# Write a program to calculate the product of the middle digits of a number?
number=int(input("enter numbers :"))
number=str(number)
mid=len(number)//2
product=int(number[mid])*int(number[mid+1])
print(product)