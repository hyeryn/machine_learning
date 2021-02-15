# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_json('./read_json_sample.json')
print(df,'\n')
print(df.index)