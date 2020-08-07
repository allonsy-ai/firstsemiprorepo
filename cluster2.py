#!/usr/bin/env python
# coding: utf-8

# In[35]:


#summon pandas as pd
import pandas as pd


# In[52]:


#using pd.read_html i convert the url into a pandas dataframe
df_toronto = pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")[0]
df_toronto


# In[53]:


df_toronto.head()


# In[55]:



#Remove Boroughs that are 'Not assigned'
canada_df = df_toronto[df_toronto['Borough'] != 'Not assigned']
canada_df.head()


# In[59]:


canada_df.rename(columns={"Postal Code": "Postcode"}, inplace=True)


# In[60]:


# More than one neighborhood can exist in one postal code area, combined these into one row with the neighborhoods separated with a comma
canada_df["Neighbourhood"] = canada_df.groupby("Postcode")["Neighbourhood"].transform(lambda neigh: ', '.join(neigh))

#remove duplicates
canada_df = canada_df.drop_duplicates()

#update index to be postcode if it isn't already
if(canada_df.index.name != 'Postcode'):
    canada_df = canada_df.set_index('Postcode')
    
canada_df.head()


# In[61]:


canada_df.shape


# In[ ]:




