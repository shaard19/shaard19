# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 00:51:43 2021

@author: $udo
"""



# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:45:21 2021

@author: $udo
"""

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
import pandas as pd
  
# creating a DataFrame
animal =  {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'], 
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3], 
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']} 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df_age = pd.DataFrame(animal)
mean = df_age.mean()
print(mean)
