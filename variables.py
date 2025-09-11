# topic :- Memory mapping 


a=34
b=34
c=34

print(id(a))
print(id(b))
print(id(c))
print(type(c))
print(type(c))

print(a==c) # comparison operator compare values of 'a' and 'c'

print(a is c) # is operator checks the memory address of 'a' and 'c'

b=a
a=a+1
print(id(b))
print(id(a))


""" 
In python we have :-

    1.Mutable data type ( Once initailized can be modified ) eg :- list[] etc.
    2.Inmutable data type (Once initialized cannot be modifed ) eg int ,string ,tupple etc .
    
"""

# list 
list= [2,3,5,2,1,3,43,5,35,53,34,3,43,434,34343,43,434,]
print(id (list))
print(list)
list.append(86)
print(list)
print(id(list))



print()  

# tupple 
tuple= 2,3,5,2,1,3,43,5,35,53,34,3,43,434,34343,43,434
c=tuple               # storing the address of the tuple 
print(id (tuple))
print(tuple )
tuple =2,3,5,2,1,3,43,5,35,53,34,3,43
print(tuple)
print(id(tuple))
print(c)              # printing the value of tuble because we have address of tuple stored in c
''' tuple does not allow modifiaction because it is an immutable data type 
    so that it make different objects with every modifictaion it means nothing 
    will be  change  in real object .The modification will happen in another object'''
    
print()

p=1;
print("ID OF P is :",id(p))
g=2
r=1;
print("ID of r is :",id(r))
s=2
print,("ID of is :",id(s))
t=p
print("ID of t is :",id(t))
u=g
print("ID of u is :",id(u))
p=p+1
print("ID of p is :",id(p))
s1="hello"
print("ID of s1 is :",id(s1))
s1="HELLO"
print("",id(s1))
s2=s1  
print("ID of s2 is :",id(s2))
s3="hii"
print("ID of s3 is :",id(s3))
print(s3.upper())

print()
print()
print()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Topic :- Interning :- python creates only a single object for the same value of a data type but for a small data or short data this is known add interning .
x="HII"
y="HII"
print(x is y )
 
 
 
 
"""Mannual interning :- When we exceed the limit of variable python make diffrent object even 
for the same value in this case we mannuals intern the data using a module called sys and a method sys.intern ."""
    
import sys
print(sys.getsizeof(42))          # int
print(sys.getsizeof("hello"))     # str
print(sys.getsizeof([1,2,3,4]))   # list


# 1. Integer
x = 42
print("Integer 42:", sys.getsizeof(x), "bytes")

# 2. String
s = "hello"
print("String 'hello':", sys.getsizeof(s), "bytes")

# 3. List
lst = [1, 2, 3, 4]
print("List [1,2,3,4]:", sys.getsizeof(lst), "bytes")

# Agar elements bhi count karein:
total = sys.getsizeof(lst) + sum(sys.getsizeof(i) for i in lst)
print("Total list (container + elements):", total, "bytes")


print()
print()
print()

#____________________________________________________________________________________________________________________________________________

#       Topic :- Opeartor  in python 

# Defination : Special symbols which is used to perform a specific task 
# Eg:- (+) symbol is used in python for operands and it performs addition or concatination depends upon the type of data 




#                    Operands 

#Defination :-On which the operation is performed 
# In programming operands are variables 
''' Types of operators
1. On the basics of no of operands
 
   a.unary operator eg:-increment operator (a=a+1,b=b+1)
   
   b. Binary operator :-No of operands 2
   eg :- additin(+) or subtraction (-)
   
   c. Ternary operator :- No of operands 3
   eg :- Logical operators (and ,or not)
      
2. On the basic of behaviour 
  a.Arithmatic 
  1.Additon (+)
  2.Subtraction (-)
  3.Division (/)
  4.Multiplication (*)
  
'''

# Assignment operator 
'''
eg a=1
   b=2
   b=a
'''
# Arithmatic Asignment operator 
'''
+=
-=
/=
*=
**=
//=

'''
a=34
b=56
a+=b 
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=2
print(a)
a**=3
print(a)

 #                             Comparison operator ;- Return true of false depend upon the expression 
 
# This means the depending statemnet executes only if we get the result 
# as per the boolean value true of false
'''
> Greater than 
>= Greater tha equals to
< less than
<= Less than equals to 
== check the value
!= not equals to  
'''
#eg 

a=5
b=3
print(a==b)
# is aperator is ued to compare the address of the variables
print(a is b)

# Logical operator:-
'''
  and :- Return true if all the contditions are true and return false even if a single condition is false 
  or  :- Return true even if a single condition is true 
  not :- Return true if a condition is false 
'''

#     conditional Operators in python 
''' 
1. if 
2. if else 
3. elif ladder
4. Match case 
5. Nested if else 

'''