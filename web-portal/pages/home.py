import dash
from dash import html, dcc


dash.register_page(__name__, path='/')

layout = html.Div(
  className='container welcome-page',
  children=[
    html.H1(children='Airbnb Predictive Model - Data Visualization'),
    html.Div(children='''
        Welcome! Please refer to the table of contents
    '''),
  ]
)