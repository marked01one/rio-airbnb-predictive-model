from dash import html, dcc
from matplotlib.figure import Figure

class QuadGraph:
  def __init__(
      self, 
      figure_1: Figure, figure_2: Figure, figure_3: Figure, figure_4: Figure, 
      className: str = None, styles: dict = None 
    ):
    self.fig_1 = figure_1
    self.fig_2 = figure_2
    self.fig_3 = figure_3
    self.fig_4 = figure_4
    self.className = className
    self.styles = styles
  
  
  def create(self):
    return \
      html.Div(
        className=self.className,
        style=self.styles,
        children=[
          
          # Top figures, including fig_1 and fig_2
          html.Div(
            className='row',
            children=[
              dcc.Graph(
                id='fig1',
                figure=self.fig_1,
                className="col-12 col-xl-6"
              ),
              dcc.Graph(
                id='fig2',
                figure=self.fig_2,
                className="col-12 col-xl-6"
              )
            ]
          ),
          
          # Bottom figures, including fig_3 and fig_4
          html.Div(
            className='row',
            children=[
              dcc.Graph(
                id='fig3',
                figure=self.fig_3,
                className="col-12 col-xl-6"
              ),
              dcc.Graph(
                id='fig4',
                figure=self.fig_4,
                className="col-12 col-xl-6"
              )
            ]
          )
        ]
      )