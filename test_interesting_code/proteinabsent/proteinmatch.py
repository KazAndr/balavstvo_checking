#!/usr/bin/env python
# coding: utf-8

# In[50]:


with open('seq_database.fasta', 'r') as file:
    content = file.readlines()


# In[51]:


with open('Term_hmmsearch.out', 'r') as file:
    term_hmmsearch = file.readlines()


# In[52]:


with open('TMP_hmmsearch.out', 'r') as file:
    tmp_hmmsearch = file.readlines()


# In[53]:


with open('MCP_hmmsearch.out', 'r') as file:
    mcp_hmmsearch = file.readlines()


# In[54]:


prot_names = []
for item in content:
    try:
        prot_name = item.split('_prot_')[0].split('|')[1]
        if prot_name not in prot_names:
            prot_names.append(prot_name)
        else:
            continue
    except IndexError:
        continue


# In[55]:


term_hmmsearch_dict = dict.fromkeys(prot_names, 0)
tmp_hmmsearch_dict = dict.fromkeys(prot_names, 0)
mcp_hmmsearch_dict = dict.fromkeys(prot_names, 0)


# In[56]:


for prot_name in prot_names:
    for line in term_hmmsearch:
        if prot_name in line:
            term_hmmsearch_dict[prot_name] +=1
    for line in tmp_hmmsearch:
        if prot_name in line:
            tmp_hmmsearch_dict[prot_name] +=1
    for line in mcp_hmmsearch:
        if prot_name in line:
            mcp_hmmsearch_dict[prot_name] +=1


# In[49]:


with open('resultsmatch.out', 'w') as file:
    file.write('Plasmids\tTerm\tTmp\tMcp\n')
    
    for prot_name in prot_names:
        file.write(f'{prot_name}\t')
        file.write(f'{term_hmmsearch_dict[prot_name]}\t')
        file.write(f'{tmp_hmmsearch_dict[prot_name]}\t')
        file.write(f'{mcp_hmmsearch_dict[prot_name]}\n')


# In[ ]:




