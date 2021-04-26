#!/usr/bin/env python
# coding: utf-8

# In[2]:


import phonenumbers
from phonenumbers import carrier, timezone, geocoder

my_number = phonenumbers.parse("+número de telefone", "BR")

print(phonenumbers.is_valid_number(my_number))
print(carrier.name_for_number(my_number, "br"))
print(timezone.time_zones_for_number(my_number))
print(geocoder.description_for_number(my_number, 'br'))


# In[3]:


# Caso não coloque um número de telefone ou sem o código do país, dará erro.


# In[4]:


# Você precisa instalar no cmd o 'pip install phonenumbers' primeiro.


# In[ ]:




