import pandas as pd

target='taro'
target='users'

df = pd.read_excel(target+'.xlsx', engine='openpyxl')

with open(target+'_gen.json', 'w', encoding='utf-8') as file:
    df.to_json(file ,orient='records', force_ascii=False)
