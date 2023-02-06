import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from constants import AXIS_FONT, TITLE_FONT
from components.charts import overview

dash.register_page(__name__, path='/literature')


df = pd.read_csv('./figures/lit_overview_frequency.csv')
num_of_articles = len(df.columns) - 4


# Page Layout
layout = html.Div(
  className='container my-4',
  children=[
    html.Div(
      className='text-center',
      children=[
        html.H1(children='Overview'),
        html.Div(children='''
          A quick overview of the most popular features, models, and data mining techniques/algorithms
        ''',
          className="my-3"
        )
      ]
    ),
    
    # Graphs for the overview page
    dcc.Graph(
      id='overview1',
      figure=overview(
        df_filtered=df[df['Category'] == 'Features'], 
        height=1500, 
        title='Most popular Airbnb features',
        labels={
          'Index': 'Airbnb Features',
          'Total': 'Number of articles',
          'Subcategory': 'Category'
        }
      )
    ),
    dcc.Graph(
      id='overview2',
      figure=overview(
        df_filtered=df[df['Category'] == 'Models'],
        height=600,
        title='Most popular machine learning models',
        labels={
          'Index': 'Models',
          'Total': 'Number of articles',
          'Subcategory': 'Category'
        }
      )
    ),
    dcc.Graph(
      id='overview3',
      figure=overview(
        df_filtered=df[df['Category'] == 'Text Mining'],
        height=500,
        title="Most popular text mining libraries/algorithms",
        labels={
          'Index': 'Text Mining Libraries/Algorithms',
          'Total': 'Number of articles',
          'Subcategory': 'Category'
        }
      )
    )
])