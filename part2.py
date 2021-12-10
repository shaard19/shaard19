#PAERT 2
#Variable declaration and initialization
variable="The quick brown fox jumped over the lazy dog"
import re

res = len(re.findall(r'\w+', variable))
  
# printing result
print(*variable.split(), sep='\n')
print ("Total of  "+  str(res))