# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름':['서준','우현','민아'],
             '수학' : [90, 80, 70], '영어' : [100, 80, 40],
             '국어' : [80, 40, 95], '미술' : [20, 75, 85]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))

# '수학' 점수 데이터만 선택. 변수 math에 저장
math = df['수학']
print(math)
print(type(math))

# '영어' 점수 데이터만 선택. 변수 english에 저장
english = df['영어']
print(english)
print(type(english))

# '국어' '미술' 점수 데이터를 선택. 변수 kor_art에 저장
kor_art = df[['국어','미술']]
print(kor_art)
print(type(kor_art))

# '수학' 점수 데이터만 선택. 변수 math2에 저장
math2 = df[['수학']]
print(math2)
print(type(math2))