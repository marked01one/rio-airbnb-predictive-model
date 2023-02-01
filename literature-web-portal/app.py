import imp
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 

stylesheets = [
  {
    'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css',
    'rel': 'stylesheet',
    'integrity': "sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD",
    'crossorigin': 'anonymous'
  }
]

app = Dash(
  __name__,
  external_stylesheets=stylesheets
)

df = pd.DataFrame({
  "Fruit": ["Apples", "Oranges", "Bananas"],
  "Amount": [4,1,2],
  "City": ['San Francisco', 'Montreal', 'New York']
})

fig = px.bar(df, x="Fruit", y="Amount")

app.layout = html.Div(children=[
  html.H1(
    children='Airbnb Predictive Model - Literature Analysis',
    style={
      "textAlign": "center",
      'color': 'blue'
    }
  ),
  
  # Subtitle text
  html.Div(
    children=[
      "For more info on this project, check out the ",
      html.A(
        children='Project GitHub',
        href='https://github.com/marked01one/rio-airbnb-predictive-model'
      )
    ], 
    style={"textAlign": "center"}
  ),
  
  # Graphs
  html.Div(
    className='my-2 mx-5 row border border-danger',
    children=[
      dcc.Graph(
        id='example-graph1',
        figure=fig,
        className="col-12 col-lg-6"
      ),
      dcc.Graph(
        id='example-graph2',
        figure=fig,
        className="col-12 col-lg-6"
      )
    ]
  ),
  
  html.P(
    children="This application is build to serve my research project in predictive modeling",
    style={
      'textAlign': "center",
      "fontStyle": "italic"
    }
  )
])

if __name__ == '__main__':
  app.run_server(debug=True)