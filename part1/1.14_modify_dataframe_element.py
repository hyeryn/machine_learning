# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = { '이름':['서준', '우현', '민아'],
             '수학':[90,80,70], '영어':[98,89,85],
             '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df,'\n')

# '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영
df.set_index('이름',inplace=True)
print(df)

# 데이터프레임 df의 특정 원소를 변경하는 방법: '서준'의 '체육' 점수
df.iloc[0][3] = 80
print(df)

df.loc['서준']['체육'] = 90
print(df)

df.loc['서준','체육'] = 100
print(df)

# 데이터프레임 df의 원소 여럭를 변경하는 방법: '서준'의 '음악','체육' 점수
df.loc['서준']['음악','체육'] = 50
print(df)

df.loc['서준']['음악','체육'] = 100, 50
print(df)
