# -*- coding: utf-8 -*-

import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터 프레임 만들기
df = pd.DataFrame([[22,'여','덕성여대'],[28,'남','대경대']],
                   index=['혜린','원필'],columns=['나이','성별','학교'])

# 행 인덱스, 열 이름 확인하기
print(df)
print(df.index)
print(df.columns)
print('\n')

# 행 인덱스, 열 이름 변경하기
df.index = ['기여운헤링','헤링남친짱필']
df.columns = ['age','sex','univ']
print(df)
print(df.index)
print(df.columns)