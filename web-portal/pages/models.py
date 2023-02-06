import dash
from dash import html, dcc, Input, Output
import plotly.express as px 
import pandas as pd
from constants import *
from components.charts import overview, categories_pie

dash.register_page(__name__, path='/literature/models')


df_freq = pd.read_csv('./figures/lit_overview_frequency.csv')
df_impact = pd.read_csv('./figures/lit_overview_impact.csv')


# ! ************ Callback functions for models overview bar charts ************

@dash.callback(Output("model_overview_freq", "figure"), Input("model_view_type_freq", "value"))
def overview_types(view_types: str):
  '''Callback function for "model overview (frequency)" bar chart
  
  ### Input:
  - `model_type: value`: View types available for choosing
  
  ### Output:
  - `overview_freq: figure`: A bar chart of all models' frequency
  '''
  return overview(
    df_filtered=df_freq[df_freq['Category'] == 'Models'],
    height=600,
    title='Most popular models (frequency)',
    labels={
      'Index': 'Models',
      'Total': 'Number of articles',
      'Subcategory': 'Category'
    },
    barmode=view_types
  )  


@dash.callback(Output("model_overview_impact", "figure"), Input("model_view_type_impact", "value"))
def overview_types(view_types: str):
  '''Callback function for "model overview (frequency)" bar chart
  
  ### Input:
  - `model_type: value`: View types available for choosing
  
  ### Output:
  - `overview_freq: figure`: A bar chart of all models' frequency
  '''
  return overview(
    df_filtered=df_freq[df_freq['Category'] == 'Models'],
    height=600,
    title='Most popular models (weighted by impact)',
    labels={
      'Index': 'Models',
      'Total': 'Impact score',
      'Subcategory': 'Category'
    },
    barmode=view_types
  )


# ! ************ Callback functions for model influence pie charts ************

@dash.callback(Output("category_freq", "figure"), Input("model_freq", "value"))
def category_types_pie(model_types: str):
  '''Callback function for "model influence per type (frequency)" pie chart
  
  ### Input:
  - `model_type: value`: All model types available for choosing (Regression, Classification, Clustering)
  
  ### Output:
  - `category_freq: figure`: A figure of models within each type and their relative influence 
  '''
  df_model_type = df_freq[df_freq['Subcategory'] == model_types]
  fig_model_type = px.pie(df_model_type, values='Total', names='Index',
                          title='Frequency')
  fig_model_type.update_layout(title_font=TITLE_FONT)
  return fig_model_type


@dash.callback(Output("category_impact", "figure"), Input("model_impact", "value"))
def category_types_pie(model_types: str):
  '''Callback function for "model influence per type (weighted by impact)" pie chart
  
  ### Input:
  - `model_type: value`: All model types available for choosing (Regression, Classification, Clustering)
  
  ### Output:
  - `category_freq: figure`: A figure of models within each type and their relative influence 
  '''
  df_model_type = df_impact[df_impact['Subcategory'] == model_types]
  fig_model_type = px.pie(df_model_type, values='Total', names='Index',
                          title='Impact')
  fig_model_type.update_layout(title_font=TITLE_FONT)
  return fig_model_type


# ! ************************ Models page layout ************************

layout = html.Div(
  className='container',
  style={'marginTop': '24px', 'marginBottom': '60px'},
  children=[
    html.Div(
      className='text-center',
      children=[
        html.H1(children='Literature Analysis - Models'),
        html.Div(children='''
          Visualizations involving all machine learning models mentioned used in the reviewed literature
        ''',
          className="my-3"
        )
      ]
    ),
    
    # Overview
    html.H2(
      "Overview",
      style=SECTION_FONT
    ),
    html.Div([
      dcc.Graph(id="model_overview_freq"),
      html.Div([
        html.P("View Options:"),
        dcc.Dropdown(
          id="model_view_type_freq",
          options=VIEW_TYPES,
          value='relative', 
          clearable=False
        )
      ], className='mx-5 px-5')
    ], className='mb-5 pb-5'),
    html.Div([
      dcc.Graph(id="model_overview_impact"),
      html.Div([
        html.P("View Options:"),
        dcc.Dropdown(
          id="model_view_type_impact",
          options=VIEW_TYPES,
          value='relative', 
          clearable=False
        )
      ], className='mx-5 px-5')
    ], className='mb-5 pb-5'),


    # Influence of each model type
    html.Div(
      className='row',
      children=[
        html.H2(
          "Influence of each model type",
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
    
    
    # Influence of each model per type
    html.Div(
      className='row',
      children=[
        html.H2(
          "Influence of each model per type",
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



