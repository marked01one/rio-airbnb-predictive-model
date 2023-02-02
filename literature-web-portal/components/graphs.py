from dash import html, dcc

class QuadGraph:
  def __init__(self, figure_1, figure_2, figure_3, figure_4):
    self.fig_1 = figure_1
    self.fig_2 = figure_2
    self.fig_3 = figure_3
    self.fig_4 = figure_4
  
  def create(self):
    return \
    html.Div(
      children=[
        
        # Top figures, including fig_1 and fig_2
        html.Div(
          className='row',
          children=[
            dcc.Graph(
              id='fig1',
              figure=self.fig_1,
              className="col-12 col-lg-6"
            ),
            dcc.Graph(
              id='fig2',
              figure=self.fig_2,
              className="col-12 col-lg-6"
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
              className="col-12 col-lg-6"
            ),
            dcc.Graph(
              id='fig4',
              figure=self.fig_4,
              className="col-12 col-lg-6"
            )
          ]
        )
      ]
    )