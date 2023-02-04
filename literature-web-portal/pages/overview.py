import dash
from dash import html, dcc
from components import graphs
from components import footer
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path='/')


df = pd.read_csv('./figures/lit_overview_transposed.csv')

fig_bar = px.bar(df, x="Features", y="Total", color='Category', height=1000)


layout = html.Div(
  className='container my-4',
  children=[
    html.H1(children='Overview'),

    html.Div(
      children='''
        The home page for the literature analysis web portal! Refer to the cards to your left for more information
    ''',
      className="my-3"
    ),
    
    # Graphs for the overview page
    dcc.Graph(
      id='overview1',
      figure=fig_bar
    )
])