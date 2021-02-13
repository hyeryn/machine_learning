# -*- coding: utf-8 -*-

# pandas 불러오기
import pandas as pd

# key:value 쌍으로 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# 판다스 Series() 함수로 dictionary를 Series로 변환. 변수 sr에 저장
sr = pd.Series(dict_data)

# sr의 자료형 출력
print(type(sr))
print('\n')
# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)