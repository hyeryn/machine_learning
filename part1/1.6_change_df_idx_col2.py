# -*- coding: utf-8 -*-

import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[22,'여','덕성여대'],[28,'남','대경대']],
                  index=['혜린','원필'],
                  columns=['나이','성별','학교'])

print(df)
print('\n')

# 변경
df.rename(columns={'나이':'age','성별':'sex','학교':'univ'}, inplace=True)
print(df)