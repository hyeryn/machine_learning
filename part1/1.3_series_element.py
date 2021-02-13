# -*- coding: utf-8 -*-

import pandas as pd

# 튜플을 시리즈로 변환 (인덱스 옵션 제외)
tup_data = ('헤링', '2000-12-01', '여', True)
sr = pd.Series(tup_data, index = ['이름','생년월일','성별','학생여부'])
print(sr)


# 원소를 1개 선택
print(sr[0])
print(sr['이름'])
print('\n')

# 여러개의 원소를 선택 (인덱스 리스트 활용)
print(sr[[1,2]])
print(sr[['생년월일','성별']])
print('\n')

# 여러개의 원소를 선택 (인덱스 범위 지정)
print(sr[1:2])
print(sr['생년월일':'성별'])