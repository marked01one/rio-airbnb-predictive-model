import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(
  className='container my-4',
  children=[
    html.H1(children='Overview'),

    html.Div(children='''
        The home page for the literature analysis web portal! \n
        Refer to the cards to your left for more information
    '''),

])