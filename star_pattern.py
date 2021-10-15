n = int(input("Enter a number: "))
a = int(input("Enter your Boolean Number: "))

if bool(a):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

else:
    for i in range(1, n + 1):
        for j in range(1, n + 2 - i):
            print("*", end="")
        print()


#   ***********Using FUnction*********

# a = int(input("Please add no of line you want to print"))
# b = int(input("Please Add 0 for false"))

# def start(a,b):
#     if b == True:
#         c = 1
#         while c <= a:
#             print(c *"*")
#             c = c + 1
#     else:
#         while a > 0:
#             print(a *"*")
#             a = a - 1

# start(a, b)
