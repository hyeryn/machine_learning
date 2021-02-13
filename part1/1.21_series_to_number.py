# -*- coding: utf-8 -*-

import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100,'영어':90,'수학':80})
print(student1)

# 학생의 과목별 점수를 100으로 나누기
percentage = student1/100

print(percentage)