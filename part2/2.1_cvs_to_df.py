# -*- coding: utf-8 -*-

import pandas as pd

# 파일 경로
file_path = './read_csv_sample.csv'

# read_cvs() 함수로 데이터프레임 변환. 변수 df1에 저장
df1 = pd.read_csv(file_path)
print(df1, '\n')

df2 = pd.read_csv(file_path, header=None)
print(df2, '\n')

df3 = pd.read_csv(file_path, index_col=None)
print(df3, '\n')

df4 = pd.read_csv(file_path, index_col='c0')
print(df4, '\n')