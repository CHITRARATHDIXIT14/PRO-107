import csv
import pandas as pd
import plotly.graph_objects as pg 

df = pd.read_csv('data.csv')
details = df.loc[df['student_id']=='TRL_mno']
fig = pg.Figure(pg.Bar(
    x = details.groupby('level')['attempt'].mean(),
    y=['level1','level2','level3','level4'],
    orientation = 'h'

))

fig.show()