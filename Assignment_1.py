#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions 
    will be mathematical operators.
* 
'hello'
-87.8
- 
()
+
6 


# In[ ]:


*=Expression
'hello'= value
-87.8= value
- = expression
(=, expression)
+ = expression
6 = value


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[ ]:


A string is a function that can be used store a value , for example , f="Name" and each character of the string has an index numer.String function is expressed in ""
whereas
A Variable is an entity which is used to store a data or a value whether it is an integer ,floating point, string, boolean etc


# In[ ]:


3.Describe three different data types.


# In[ ]:


String, List, Tuple


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


expressions are mostly made of variables and mathematical operators and are used as per the logic of the problem statement for solving an arthematical problem.The expressions yields either sum , difference, product or quotient based on the operator used in the logic.


# In[ ]:


get_ipython().set_next_input('5.This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')


# In[ ]:


Expressions are made of variables and mathematical operators whereas statement is a command that is used by the python to execute.


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


# In[3]:


bacon = 22


# In[4]:


bacon


# In[5]:


bacon+1


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' * 3


# In[6]:


'spam' + 'spamspam'


# In[7]:


'spam' * 3


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')


# In[ ]:


eggs can be assigned with numbers for eg: eggs = 1000
    whereas numbers cannot be aasigned with other numbers ie 100 = 1000 is invalid logic


# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')


# In[21]:


a= 10.5


# In[22]:


int(a)


# In[23]:


float(a)


# In[24]:


str(a)


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'


# In[25]:


'I have eaten ' + 99 + ' burritos.'


# In[27]:


"'I have eaten ' + 99 + ' burritos.'"


# In[ ]:


By adding "" the error can be avoided , '' quotes can be treated as apostrophes by python program which causes error.

