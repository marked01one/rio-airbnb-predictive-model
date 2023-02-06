import pandas as pd 
import plotly.express as px
from constants import AXIS_FONT, TITLE_FONT


def overview(df_filtered: pd.DataFrame, height: int, title: str, labels: dict = None):
  df = df_filtered.sort_values(by=['Total'])

  fig = px.bar(df, x="Total", y="Index", color='Subcategory', orientation='h', barmode='relative',
                        labels=labels, height=height, title=title)
  fig.update_layout(title_font=TITLE_FONT)
  fig.update_yaxes(categoryorder='total ascending', titlefont=AXIS_FONT)
  fig.update_xaxes(titlefont=AXIS_FONT)
  
  return fig