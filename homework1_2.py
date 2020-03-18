#!/usr/bin/env python
# coding: utf-8

# In[169]:


#from collections.abc import Sequence
import random
from random import randint
from array import typecodes

import numpy

import array

class ArrayList():

    def __init__(self):
        self.length = randint(10,20)
        self.data = array.array('i',[randint(0,200) for i in range(self.length)])
#не получается сделать и целые, и строки, и вещественные. array.array может ли только i-int,
#u-str или f-float иметь в TypeCode. Я думала, создать отдельно строки, числа и объединить, 
#но так вряд ли нужно

    def __len__(self):
        return self.length
  
    def __iter__(self):
        return (i for i in self.data)
    
    def __reversed__(self):
        return (self.data[i] for i in range(self.length-1,-1,-1))
    
    def __getitem__(self, val): 
        return self.data[val] 

    def __contains__(self, item):
            return item in self.data

    def count(self,c):
        k=0
        for i in self.data:
            if c==i:
                k+=1
        return k

    def index(self, c, start,end):
        f=0
        for i in range(start,end):
            if c==self.data[i]:
                ind=i
                f=1
                return ind
        if f==0:
            return 'did not find' 


# In[170]:


al=ArrayList()


# In[171]:


# len also works

print('***length = ', end=' ')

print(len(al))


# In[172]:


#iter works

print('***iter works')

for i in al:
    print(i)


# In[173]:


#итерация в обратном порядке:reversed

print('***reversed works')

for i in range(len(al)-1,-1,-1):

    print(al[i])


# In[174]:


# getitem works

print('***getitem works')

print('al[0] is ', al[0])


# In[180]:


print('al[0:10:2] is ', al[0:len(al)].tolist())


# In[181]:


#есть ли в нашем массиве 100

print('***contains works')

print('does al contains 100: ',end=' ')

print(100 in al)


# In[182]:


#проверка принадлежности нулевого элемент массиву(должно быть,конечно, TRUE)

a = al[0]

print('does al contains a=al[0]: ',end=' ')

print(a in al)


# In[183]:


#поиск количевств вхождений 171 и нулевого элемента

print('***count works')

print('count of 171: ',al.count(171))


# In[184]:


#поиск количевств вхождений нулевого элемента
print('count of al[0]: ',al.count(al[0]))


# In[185]:



#поиск первого индекса вводимого элемента, вид: (элемент, начало,конец поиска)

#если нет вхождений возвращает ´did not find'

print('***index works')

print('index of 24: ',al.index(24,0,len(al)))


# In[186]:


print('index of al[0]: ',al.index(al[0],0,len(al)))


# In[ ]:




