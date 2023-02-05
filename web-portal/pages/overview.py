import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from constants import AXIS_FONT, TITLE_FONT

dash.register_page(__name__, path='/literature')


df = pd.read_csv('./figures/lit_overview_frequency.csv')
num_of_articles = len(df.columns) - 4



# Features Overview DataFrame & Graph
df_features = df[df['Category'] == 'Features'].sort_values(by=['Total'])

fig_features = px.bar(df_features, x="Total", y="Index", color='Subcategory', orientation='h', barmode='relative',
                      labels={
                        'Index': 'Airbnb Features',
                        'Total': f'Number of articles (out of {num_of_articles})',
                        'Subcategory': 'Category'
                      },
                      height=1500, title='Most popular features (descending order)')
fig_features.update_layout(title_font=TITLE_FONT)
fig_features.update_yaxes(categoryorder='total ascending', titlefont=AXIS_FONT)
fig_features.update_xaxes(titlefont=AXIS_FONT)



# Models Overview DataFrame & Graph
df_models = df[df['Category'] == 'Models'].sort_values(by=['Total'])

fig_models = px.bar(df_models, x="Total", y="Index", color='Subcategory', orientation='h', barmode='group',
                      labels={
                        'Index': 'Models',
                        'Total': f'Number of articles (out of {num_of_articles})',
                        'Subcategory': 'Category'
                      },
                      height=800, title='Most popular models (descending order)')
fig_models.update_layout(title_font=TITLE_FONT)
fig_models.update_yaxes(categoryorder='total ascending', titlefont=AXIS_FONT)
fig_models.update_xaxes(titlefont=AXIS_FONT)



# Models Overview DataFrame & Graph
df_mining = df[df['Category'] == 'Data Mining'].sort_values(by=['Total'])

fig_mining = px.bar(df_mining, x="Total", y="Index", color='Subcategory', orientation='h', barmode='relative',
                      labels={
                        'Index': 'Data Mining Libraries/Algorithms',
                        'Total': f'Number of articles (out of {num_of_articles})',
                        'Subcategory': 'Category'
                      },
                      height=600, title='Most popular data mining libraries/algorithms (descending order)')
fig_mining.update_layout(title_font=TITLE_FONT)
fig_mining.update_yaxes(categoryorder='total ascending', titlefont=AXIS_FONT)
fig_mining.update_xaxes(titlefont=AXIS_FONT)



# Page Layout
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
      figure=fig_features
    ),
    dcc.Graph(
      id='overview2',
      figure=fig_models
    ),
    dcc.Graph(
      id='overview3',
      figure=fig_mining
    )
])