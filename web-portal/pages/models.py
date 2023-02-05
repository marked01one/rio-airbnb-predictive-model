import dash
from dash import html, dcc
import plotly.express as px 
import pandas as pd

dash.register_page(__name__, path='/literature/models')

layout = html.Div(
  className='container my-4',
  children=[
    html.H1(children='Literature Analysis - Models'),
    html.Div(children='''
        Literature Analysis Web Portal
    '''),

])