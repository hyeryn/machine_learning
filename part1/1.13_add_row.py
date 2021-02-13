# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = { '이름':['서준', '우현', '민아'],
             '수학':[90,80,70], '영어':[98,89,85],
             '음악':[85,95,100], '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df,'\n')

# 새로운 행(row) 추가. 같은 원소 값 입력
df.loc[3] = 0
print(df)

# 새로운 행 추가. 원소 값 여러개의 배열 입력
df.loc[4] = ['동규',30,40,50,70]
print(df)

# 새로운 행 추가. 기존 행 복사
df.loc['4-1'] = df.loc[4]
print(df)