# -*- coding: utf-8 -*-

import pandas as pd

# 판다스 DataFrame() 힘수로 데이터프레임 변환. 변수 df에 저장
data = {'name' : ['Jerry', 'Rian', 'Paul'],
        'algol' : ['A+', 'A', 'B+'],
        'basic' : ['C', 'B', 'B'],
        'C++' : ['B+', 'C', 'C']}

df = pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)

# to_excel() 메소드를 사용하여 Excel 파일로 내보내기. 파일명은 df_sample.xlsx로 저장
df.to_excel("./df_sample.xlsx")