#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')


# In[ ]:


1 and 0
True and False


# In[ ]:


get_ipython().set_next_input('What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')


# In[ ]:


and, or , not


# In[ ]:


Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).


# In[ ]:


True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False


# In[ ]:


get_ipython().set_next_input('What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)


# In[1]:


print((5 > 4) and (3 == 5))


# In[2]:


print(not (5 > 4))


# In[3]:


print((5 > 4) or (3 == 5))


# In[4]:


print(not ((5 > 4) or (3 == 5)))


# In[5]:


print((True and True) and (True == False))


# In[6]:


print((not False) or (not True))


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')


# In[ ]:


==
<
>
>=
<=
get_ipython().system('=')


# In[ ]:


get_ipython().set_next_input('6. How do you tell the difference between the equal to and assignment operators');get_ipython().run_line_magic('pinfo', 'operators')
Describe a condition and when you would use one.


# In[9]:


if (5==4) and (6>=3):
    print("True")
else:
    print("False")


# In[ ]:


Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


# In[14]:


spam = 0
if spam == 10:
    print('eggs') #block 1
    if spam > 5:
        print('bacon') #block 2
else:
    print('ham') # block 3
    print('spam')
    print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam,
prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


# In[24]:


spam=int(input("Enter a number"))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')


# In[ ]:


ctrl+c


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')


# In[33]:


for i in range(5):
    if(i==3):
        break
    print(i)
print("\n")
for i in range(5):
    if(i==3):
        continue
    print(i)
print("\n")


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[34]:


n=10
for i in range(10):
    print(i)


# In[35]:


n=10
for i in range(0,10):
    print(i)


# In[36]:


n=10
for i in range(0,10,1):
    print(i)


# In[ ]:


All the above 3 syntax gives the same output


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop.
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.


# In[5]:


n=11
for i in range(1,11,1):
    print(i)


# In[3]:


n =1
while n <= 10:
    print(n)
    n+=1


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


spam.bacon()

