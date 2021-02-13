# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학':[90,80,70],'영어':[98,89,95],
             '음악':[40,50,20],'체육':[40,20,50]}

df = pd.DataFrame(exam_data, index = ('서준','우현','민아'))
print(df,'\n')

# 행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print(position1)

# 행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['서준','민아']]
position2 = df.iloc[[0,2]]
print(label2)
print(position2)

# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3)
print(position3)