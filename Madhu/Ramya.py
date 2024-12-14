import pandas as pd
df=pd.read_excel('/workspaces/AIES-Innovation-Lab/Madhu/EXTERNAL DUTY - REQUIREMENTS.xlsx')
print(df.isnull().sum())