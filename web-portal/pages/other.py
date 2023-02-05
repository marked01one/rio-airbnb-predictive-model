import dash
from dash import html, dcc


dash.register_page(__name__, path='/literature/other')

layout = html.Div(
  className='container my-4',
  children=[
    html.H1(children='Literature Analysis - Other Visualizations'),
    html.Div(children='''
        Other visualizations of our literature analysis
    '''),
  ]
)