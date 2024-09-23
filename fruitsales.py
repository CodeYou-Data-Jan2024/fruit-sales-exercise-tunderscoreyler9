# add your code here
import pandas as pd

data = {
    'Apples': [35, 41],
    'Bananas': [21, 34],
}

index = ['2017 Sales', '2018 Sales']

df = pd.DataFrame(data, index=index)
df.to_csv('fruit.csv')

print("`fruitsales.py` has written data to `fruit.csv`!")