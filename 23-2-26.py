# Function
# def sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# sum(5, 8)
# sum(53, 48)
# sum(59, 84)

# Average of 3 numbers
# def avg(a,b,c):
#     sum = a + b +c
#     avg = sum/3
#     print(avg)

# avg(5,8,1)

# WAF to print the length of a list
# cities = ["Gujranwala", "Lahore", "Karachi", "Quetta", "Sialkot", "Gujrat"]
# marks = [76,93,64,96,67]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(marks)

# WAF to print the factorial of a number
# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# fact(8)

# WAF to convert USD to PKR
# def converter(usd_val):
#     pkr_val = usd_val * 280
#     print(usd_val,"USD =", pkr_val, "PKR")

# converter(29)

# Write to function to check the number odd or even
# def check(n):
#     if(n%2==0):
#         print("Even.")
#     else:
#         print("Odd.")

# n = int(input("Enter a number: "))
# check(n)

# Recursion
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# WAP to show factorial using recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(5))

# WAP to print the sum of n numbers using recursion
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1)+n
# n = sum(8)
# print(n)