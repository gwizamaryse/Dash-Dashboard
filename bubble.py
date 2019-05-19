import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Data/mpg.csv')

print(df)

data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker= dict(size=3*df['cylinders'],
                    color=df['cylinders'],
                    showscale=True))]
layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
