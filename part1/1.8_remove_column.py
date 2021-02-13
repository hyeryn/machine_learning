# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학':[90,80,70],'영어':[98,89,95],
             '음악':[40,50,20],'체육':[40,20,50]}

df = pd.DataFrame(exam_data, index = ('서준','우현','민아'))
print(df,'\n')

# 데이터프레임 df를 복제하여 변수 df4에 저장. df4의 1개 열(column) 삭제
df4 = df[:]
df4.drop('수학',axis=1 ,inplace=True)
print(df4)

# 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 2개 열(column) 삭제
df5 = df[:]
df5.drop(['영어','음악'], axis=1, inplace=True) # axis = 1은 열 삭제 
print(df5)