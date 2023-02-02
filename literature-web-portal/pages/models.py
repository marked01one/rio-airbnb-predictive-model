import dash
from dash import html, dcc

dash.register_page(__name__, path='/models')

layout = html.Div(
  className='container my-4',
  children=[
    html.H1(children='Models'),
    html.Div(children='''
        Literature Analysis Web Portal
    '''),

])