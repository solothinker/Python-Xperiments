import numpy as np
# printing field name 
for ii, jj in enumerate(vars(np)):
    print(ii,':-',jj)
# getting help 
hlp = help(np.mat)
print(hlp)
