#!/usr/bin/env python
# coding: utf-8

# In[1]:


def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')


# In[2]:


import numpy as np
def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


# In[3]:


img ="http://static.cricinfo.com/db/PICTURES/CMS/263600/263697.20.jpg"


# In[4]:


import imageio
s = imageio.imread(img)
g=grayscale(s)
i = 255-g
import scipy.ndimage
b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r= dodge(b,g)


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.imshow(r, cmap="gray")


# In[6]:


plt.imsave('img2.png', r, cmap='gray', vmin=0, vmax=255)


# In[ ]:





# In[ ]:




