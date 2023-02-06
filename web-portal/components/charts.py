import pandas as pd 
import plotly.express as px
from constants import MODEL_CAT
from constants import AXIS_FONT, TITLE_FONT
from matplotlib.figure import Figure


def overview(df_filtered: pd.DataFrame, height: int, title: str, labels: dict = None, barmode: str = 'relative') -> Figure:
  df = df_filtered.sort_values(by=['Total'])

  fig = px.bar(df, x="Total", y="Index", color='Subcategory', orientation='h', barmode=barmode,
                        labels=labels, height=height, title=title)
  fig.update_layout(title_font=TITLE_FONT)
  fig.update_yaxes(categoryorder='total ascending', titlefont=AXIS_FONT)
  fig.update_xaxes(titlefont=AXIS_FONT)
  
  return fig



def categories_pie(df: pd.DataFrame, title: str) -> Figure:
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