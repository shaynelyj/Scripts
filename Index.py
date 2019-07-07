#!/usr/bin/env python
# coding: utf-8

# In[19]:


q=int(input("q:"))
p=int(input("p:"))
n=int(input("n:"))
#d=int(input("d:"))
#e=int(input("e:"))
#m=int(input("m:"))
#c=int(input("c:"))


# In[20]:


def return_q():
    if q:
        return(q)
    else:
        try:
            return(n/p)
        except:
            return("-")


# In[ ]:


def return_p():
    if p:
        return(p)
    else:
        try:
            return(n/q)
        except:
            return("-")


# In[21]:


print(f"q={return_q()}")


# In[ ]:




