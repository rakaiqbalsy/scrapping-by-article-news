#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from newspaper import Article


# In[21]:


def scrap_data(url: str) -> tuple:
    str_text = Article(url)
    str_text.download()
    str_text.parse()
    nltk.download('punkt')
    str_text.nlp()
    data = str_text.text
    author = str_text.authors
    publish = str_text.publish_date
    # raw_text = views.result(data)
    return data, author, publish

    


# In[24]:


url = "https://www.vice.com/id_id/article/m7jy3a/pelajaran-sejarah-bakal-tidak-diwajibkan-di-kurikulum-2020-asosiasi-guru-indonesia-protes"
data = scrap_data(url)


# In[25]:



print(data)


# In[ ]:




