import dash
from dash import html, dcc

dash.register_page(__name__, path='/features')

layout = html.Div(
  className='container my-4',
  children=[
    html.H1(children='Features'),
    html.Div(children='''
        Visualizations involving quantitative/qualitative features of Airbnb listings used in the reviewed literature
    '''),

])