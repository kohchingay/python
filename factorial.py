#!/usr/bin/env python
# coding: utf-8

# In[9]:


import streamlit as st

def factorial():
    n = int(input("Enter an integer:"))
    initial=n
    result=n
    for i in range(n-2):
        result=result*(n-1)
        n-=1
        print(result)
    print(f"\nThe factorial of {initial} is {result}.")

factorial()


# In[ ]:




