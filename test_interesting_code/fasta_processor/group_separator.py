#!/usr/bin/env python
# coding: utf-8

# In[36]:


import os
from collections import defaultdict


# In[47]:


cont_dict = defaultdict(type([]))
cut_level = int(input('Введите число отсечки для групп: '))


# In[48]:


with open('config.py', 'r') as conf:
    inform_line = conf.readline()
    paths = conf.readlines()


# In[49]:


for path in paths:
    with open(path, 'r') as file:
        content = file.readlines()
    
    for i in content:
        if len(i) <= 15: # Обратить особое внимание на то, что для других файлов это число может быть иным
            name_group = i
            cont_dict[name_group]
        else:
            cont_dict[name_group].append(i)
    
    group_number = 1    
    for key in cont_dict.keys():
        if len(cont_dict[key])/2 >= cut_level:
            # Проверяем существует ли директория и если нет, то создаем
            res_dir = f'result_from_{path}'
            if not os.path.isdir(res_dir):
                os.mkdir(res_dir)
            
            with open(
                f'{res_dir}/group_{group_number}_from_{os.path.basename(path)}.fasta', 'w'
            ) as res:
                res.write(key)
                for item in cont_dict[key]:
                    res.write(item)
            group_number += 1


# In[17]:





# In[18]:





# In[30]:





# In[31]:





# In[ ]:




