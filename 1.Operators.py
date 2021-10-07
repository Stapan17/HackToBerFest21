# 1. ARITHMETIC OPERATORS
print("********1.ARITHMETIC OPERATORS********")

a = 5
b = 2

# print(a+b)
print(f"The sum of {a+b}")
print(f"The subtraction of {a-b}")
print(f"The multiplication of {a*b}")
print(f"The devision of integer value {a//b}") #it return less value closer than original value
print(f"The devision of float value  {a/b}")


# 2. RELATIONAL  OPERATORS OR COMPARISION OPERATOR
print("********2.COMPARISION OPERATORS********")

print(f"The number equal to {a==b}")
print(f"The number not equal to {a!=b}")
print(f"The number is greater than a {a>b}")
print(f"The number is greater than equal to a {a>=b}")
print(f"The number is less than than equal to a {a<=b}")


# 3. ASSIGNMENT OPERATORS
print("********3.ASSIGNMENT OPERATORS********")
# it is used to assign values to variable

print(f"Assign the value of a {a+5}")
print(f"Assign the value of a {a-5}")
print(f"Assign the value of a {a*5}")
print(f"Assign the value of a {a/5}")
print(f"Assign the value of a {a//5}")


# 4. ASSIGNMENT OPERATORS
print("********4.SPECIAL OPERATORS********")

# 1. Identity Operators IS and IS NOT are the identity operators
c= 6
d = 6

e = [3,5,6]
f = [3,5,6]

g = "khand"
h = "khand"

print(f"for single value memory allocate c == d {c is d}")
print(f"for multiple value memory allocate e == f {e is f}")
print(f"for single value memory allocate g == h {g is not h}")

# 2. Membership Operators IN and NOT IN are membership iperators 
dic = {1:"a", 2:"b", 3:"c"}
print(f"5 is present in e list {5 in e}")
print(f"5 is present in dic dictionary {2 not in dic}")


  
# 5. BITWISE  OPERATORS 
x = 10 
y = 4

print(f" for and operator {x & y}")
print(f" for or operator {x | y}")
print(f" for xor operator {x ^ y}")
print(f" for bitwise 1's complement operator {~y}")
print(f" for bitwise left shift operator {x<<y}")
print(f" for bitwise right shift operator {x>>y}")




