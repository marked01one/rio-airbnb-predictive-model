import dash
from dash import html, dcc
import pandas as pd 
import plotly.express as px
from constants import SECTION_FONT 
from components.charts import overview, categories_pie

dash.register_page(__name__, path='/literature/features')


df_freq = pd.read_csv('./figures/lit_overview_frequency.csv')
df_impact = pd.read_csv('./figures/lit_overview_impact.csv')


# ! ************************ Features page layout ************************

layout = html.Div(
  className='container my-4',
  children=[
    html.Div(
      className='text-center',
      children=[
        html.H1(children='Literature Analysis - Features'),
        html.Div(children='''
            Visualizations involving quantitative/qualitative features of Airbnb listings used in the reviewed literature
        ''')
      ]
    ),
    
    # Overview graphs
    html.H2(
      "Overview:",
      style=SECTION_FONT
    ),
    dcc.Graph(
      id='feature-overview1',
      figure=overview(
        df_filtered=df_freq[df_freq['Category'] == 'Features'], 
        height=1400, 
        title='Most popular Airbnb features (frequency)',
        labels={
          'Index': 'Airbnb Features',
          'Total': 'Number of articles',
          'Subcategory': 'Category'
        }
      )
    ),
    dcc.Graph(
      id='feature-overview2',
      figure=overview(
        df_filtered=df_impact[df_impact['Category'] == 'Features'],
        height=1400,
        title='Most popular Airbnb features (weighted by impact)',
        labels={
          'Index': 'Airbnb Features',
          'Total': 'Impact score',
          'Subcategory': 'Category'
        }
      )
    )
  ]
)