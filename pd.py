import pandas as pd
data={'calories':[340,420,340],
      'duration':[30,40,45]}
var=pd.DataFrame(data,index=['day1','day2','day3'])
print(var)