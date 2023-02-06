import dash
from dash import html, dcc, Input, Output
import plotly.express as px 
import pandas as pd
from constants import *
from components.charts import overview

dash.register_page(__name__, path='/literature/models')


df_freq = pd.read_csv('./figures/lit_overview_frequency.csv')
df_impact = pd.read_csv('./figures/lit_overview_impact.csv')
num_of_articles = len(df_freq.columns) - 4


@dash.callback(Output("category_freq", "figure"), Input("model_freq", "value"))
def category_types_pie(model_types: str):
  df_model_type = df_freq[df_freq['Subcategory'] == model_types]
  fig_model_type = px.pie(df_model_type, values='Total', names='Index',
                          title='Frequency')
  fig_model_type.update_layout(title_font=TITLE_FONT)
  return fig_model_type


@dash.callback(Output("category_impact", "figure"), Input("model_impact", "value"))
def category_types_pie(model_types: str):
  df_model_type = df_impact[df_impact['Subcategory'] == model_types]
  fig_model_type = px.pie(df_model_type, values='Total', names='Index',
                          title='Impact')
  fig_model_type.update_layout(title_font=TITLE_FONT)
  return fig_model_type


def categories_pie(df: pd.DataFrame, title: str):
  # Get total lists for each model category
  totals_lists = [
    df[df['Subcategory'] == model]['Total'].to_list()
    for model in MODEL_CAT
  ]
  
  # Convert all arrays in `totals_lists` with actual total
  for i in range(3):
    cat_sum = 0
    for tot in totals_lists[i]:
      cat_sum += int(tot)
    
    totals_lists[i] = cat_sum  
  
  # Create totals DataFrame
  df_totals = pd.DataFrame({'Category': MODEL_CAT, 'Total': totals_lists})
  fig = px.pie(
    df_totals, values='Total', names='Category',
    title=title
  )
  fig.update_layout(title_font=TITLE_FONT)
  
  
  
  return fig



layout = html.Div(
  className='container',
  style={'marginTop': '24px', 'marginBottom': '60px'},
  children=[
    html.Div(
      className='text-center',
      children=[
        html.H1(children='Literature Analysis - Models'),
        html.Div(children='''
            This page includes visualizations about all models mentioned in papers that we have reviewed
        ''')
      ]
    ),
    html.H2(
      "Overview:",
      style=SECTION_FONT
    ),
    dcc.Graph(
      id='model-overview1',
      figure=overview(
        df_filtered=df_freq[df_freq['Category'] == 'Models'],
        height=800,
        title='Most popular models (frequency)',
        labels={
          'Index': 'Models',
          'Total': 'Number of articles',
          'Subcategory': 'Category'
        }
      )
    ),
    dcc.Graph(
      id='model-overview2',
      figure=overview(
        df_filtered=df_impact[df_impact['Category'] == 'Models'],
        height=800,
        title='Most popular models (weighted by impact)',
        labels={
          'Index': 'Models',
          'Total': 'Number of articles',
          'Subcategory': 'Category'
        }
      )
    ),
    html.Div(
      className='row',
      children=[
        html.H2(
          "Part 1 - Influence within each model type",
          style=SECTION_FONT
        ),
        html.Div(
          className='col-12 col-lg-6',
          children=[
            dcc.Graph(figure=categories_pie(df_freq, 'Frequency'))
          ]
        ),
        html.Div(
          className='col-12 col-lg-6',
          children=[
            dcc.Graph(figure=categories_pie(df_impact, 'Impact'))
          ]
        ),
      ]
    ),
    html.Div(
      className='row',
      children=[
        html.H2(
          "Part 2 - Influence within each model type",
          style=SECTION_FONT
        ),
        html.Div(
          className='col-12 col-lg-6',
          children=[
            dcc.Graph(id="category_freq"),
            html.Div(
              children=[
                html.H5("Model Categories:"),
                dcc.Dropdown(
                  className='col-6',
                  id="model_freq",
                  options=MODEL_CAT,
                  value='Regression', clearable=False,
                )
              ]
            )
          ]
        ),
        html.Div(
          className='col-12 col-lg-6',
          children=[
            dcc.Graph(id="category_impact"),
            html.Div(
              children=[
                html.H5("Model Categories:"),
                dcc.Dropdown(
                  className='col-6',
                  id="model_impact",
                  options=MODEL_CAT,
                  value='Regression', clearable=False,
                )
              ]
            )
          ]
        )
      ]
    )
  ]
)



