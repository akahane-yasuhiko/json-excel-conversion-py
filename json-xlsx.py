# import json
import pandas as pd

target='taro'
target='users'

df = pd.read_json(target+'.json')

# 配列を表形式にするうまい方法がない。以下で頑張ってる例もあるがカラムになられても困る。。
# # https://stackoverflow.com/questions/37706351/nested-json-to-csv-generic-approach
# with open(target+'.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
# df = pd.json_normalize(data)

df.to_excel(target+'_gen.xlsx', index=False, header=True)
