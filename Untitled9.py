#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Candidates - Question 1
#You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.
#For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']
n=int(input("Enter the number of element in a list: "))
List=[]
for i in range(n):
    strings=input("Enter the string: ")
    List.append(strings)
List.sort(key=lambda x: x[-2])
print(List)
    
 


# In[9]:


#Your task is to complete the validate_triangle and validate_rectangle functions for the classes. 
class shape:
    def __init__(self,sides):
        self.sides=sides
        
    def validate_triangle(self):
        a, b, c = sorted(self.sides)
        if a+b>c:
            print("valid triangle")
        else:
            print("invalid triangle")
    
    def validate_rectangle(self):
        if len(self.sides) == 4:
            a, b, c, d = self.sides
            if a == c and b==d:
                print("valid rectangle")
            else:
                print("invalid rectangle")
        else:
            print("invalid rectangle")
triangle=shape([3,4,5])
triangle.validate_triangle()
rectangle=shape([2,4,2,4])
rectangle.validate_rectangle()


# In[ ]:




