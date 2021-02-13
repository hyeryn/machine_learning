# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.tail())  # 마지막 5행 표시
print(type(df))

# 데이터프레임에 숫자 10더하기
addition = df + 10
print(addition.tail())
print(type(addition))

# 데이터프레임끼리 연산하기
substraction = addition - df
print(substraction.tail())
print(type(substraction))