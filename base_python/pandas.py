#importing pandas
import pandas as pd
#creating dictionary
data={"English_Marks":[89,85,92,94,99],
"Maths_Marks":[78,82,91,67,89]}
#creating DataFrame from dictionary
df=pd.DataFrame(data)
#printing DataFrame
print(df)