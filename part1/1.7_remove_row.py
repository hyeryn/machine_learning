# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학':[90,80,70],'영어':[98,89,95],
             '음악':[40,50,20],'체육':[40,20,50]}

df = pd.DataFrame(exam_data, index = ('서준','우현','민아'))
print(df,'\n')

# 데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 행(row) 삭제
df2 = df[:]
df2.drop('우현',inplace=True)
print(df2)

# 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row) 삭제
df3 = df[:]
df3.drop(['우현','민아'], axis=0, inplace=True) # axis = 0은 행 삭제 
print(df3)