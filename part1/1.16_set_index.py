# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = { '이름':['서준', '우현', '민아'],
             '수학':[90,80,70], '영어':[98,89,85],
             '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df,'\n')

# 특정 열을 데이터프레임의 행 인덱스로 설정
ndf = df.set_index(['이름'])
print(ndf)
ndf2 = ndf.set_index('음악')
print(ndf2)
ndf3 = ndf.set_index(['음악','체육'])
print(ndf3)