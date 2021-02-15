# -*- coding: utf-8 -*-

import pandas as pd

url = './sample.html'

# html 웹페이지의 표를 가져와서 데이터프레임으로 변환
tables = pd.read_html(url)

print(len(tables),'\n')

# 테이블  리스트의 원소를 iteration하면서 각각 화면에 출력
for i in range(len(tables)):
    print("tables[%s]" %i)
    print(tables[i],'\n')
    
# 파이썬 패키지 정보가 들어있는 두 번째 데이터프레임을 선택하여 df 변수에 저장
df = tables[1]

# 'name'열을 인덱스로 지정
df.set_index(['name'],inplace=True)
print(df)