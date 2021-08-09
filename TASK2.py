#!/usr/bin/env python
# coding: utf-8

# # TASK 2
# # REFERRAL ID:SIRSS2159
# ## FULL NAME : SHEREEN ANTHONY

# In[11]:


a = lambda str: str.split()[0]
str = "hello world"
print(a(str))


# In[12]:


def splt(s):
    return s.split()[0]
str = "The greatest glory in living lies not in never falling, but in rising every time we fall."
splt(str)


# In[13]:


lst = ['Love For All', 'Hatred For None']
s = list(map(lambda a: a.split()[0],lst))
print(s)


# In[14]:


def prime(a):
    fact = []
    div = 2
    while div <= a:
        if a%div == 0:
            fact.append(div)
            a = a/div
        else:
            div += 1 
    return fact

n = input('Enter the number: ')
print(prime(int(n)))


# In[15]:


list1 = []
 
def second_largest(l):
    new_list = set(l)
    new_list.remove(max(new_list))
    return max(new_list)

for i in range(1, 5):
    elmnt = int(input("Enter elements: "))
    list1.append(elmnt)
    
print('All elements: ',list1)
print('2nd largest element: ',second_largest(list1))


# In[ ]:




