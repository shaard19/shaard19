# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:26:32 2021

@author: $udo
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:32:29 2021

@author: $udo
"""
# importing pandas as pd
import pandas as pd
  
# Check the version of the dependencies
pd.show_versions()
# importing library
import pandas as pd
import numpy as np
  
# importing the modules
from IPython.display import display
import pandas as pd
  
# creating a DataFrame
data =  {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'], 
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3], 
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']} 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data)
df3 = df.iloc[[0, 1, 2]]
# show the dataframe
df3
  
# displaying the DataFrame
display(df3)