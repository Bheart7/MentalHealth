import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

df = pd.read_csv('Data/new.csv')

df1 = df[['self_employed','treatment','family_history']]

df2 = df[['Country','self_employed','treatment','family_history']]



app.layout = html.Div([


    dcc.Dropdown(id='understand',options=[{'label':i.title(), 'value':i} for i in df1],
    value='self_employed'

        ),


    dcc.Graph(id='understand-graph')


])

@app.callback(Output('understand-graph','figure'),[Input('understand','value')])

def update(xaxis_name):
      return{

      'data':[go.Bar(
                    x=pd.crosstab(index=df2['Country'], columns=df2[xaxis_name]).index,
                    y=pd.crosstab(index=df2['Country'], columns=df2[xaxis_name])['Yes'],
                    name='Yes',
                    marker={'color':'#FFD700'}),
            go.Bar(
                    x=pd.crosstab(index=df2['Country'], columns=df2[xaxis_name]).index,
                    y=pd.crosstab(index=df2['Country'], columns=df2[xaxis_name])['No'],
                    name='No',
                    marker={'color':'#FF69B4'})],
      'layout':go.Layout(title=xaxis_name,
      xaxis={'title':'Country'},
      yaxis={'title':'Count'})
    }

if __name__ == '__main__':
    app.run_server()
