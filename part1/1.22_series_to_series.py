# -*- coding: utf-8 -*-

import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100,'영어':90,'수학':80})
student2 = pd.Series({'수학':80, '국어':90,'영어':60})
print(student1)
print(student2)

# 두 학생의 과목별 점수로 사칙연산 수행
add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2
print(div)

# 사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
result = pd.DataFrame([add,sub,mul,div],index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)