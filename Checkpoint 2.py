#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
ch=""
for i in range (2000,3201):
    if i%7==0 and i%5!=0:
     ch=ch+" "+str(i)
print(ch)


# In[2]:


#Question 2 :
n=int(input("donner un nombre: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print (fact)


# In[3]:


#Question 3 :
d={}
n=int(input("donner un nombre: "))
for i in range (1,n+1):
    d[i]=i*i
    print(d)


# In[4]:


#Question 4:
word=str(input("saissisez le mot: "))
n=int(input("saissiez l\'élement souhaité être supprimé: "))
if n < 0 and n > len(word):
    print("wrong process")
else:
    remove_char=word[ :n]+word[n+1:]
    print(remove_char)


# In[6]:


#Question 5 :
import numpy as np
a=np.array([[0,1],[2,3],[4,5]])
l=a.tolist()
print(l)


# In[7]:


#Question 6:
import numpy as np
OA1=np.array([0,1,2])
OA2=np.array([2,1,0])
cov_mat = np.stack((OA1,OA2), axis = 0) 
print(np.cov(cov_mat))  


# In[8]:


#Question 7:
import math
C=50
H=30   
resultat_final=[]
valeurs = input("saisissez les valeurs: ")
L=valeurs.split(",")
for i in L:
        resultat=math.sqrt((2*C*int(i)/H))
        resultat_final.append(round(resultat))
print (resultat_final)
    


# In[ ]:




