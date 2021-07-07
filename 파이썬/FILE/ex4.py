#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_len(l):
    total = 0
    for i in l :
        total += 1
    return total


# In[2]:


a = [5,5,6,7,8,3]
b = 'Life is short.'
print(len(a),len(b))
print(my_len(a), my_len(b))


# In[3]:


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


# In[4]:


a=1
b=2
c=add(a,b)
d=sub(a,b)
e=mul(a,b)
f=div(a,b)
print(c,d,e,f)


# In[ ]:




