from dash import html, dcc
import dash


class Sidebar:
  def __init__(self, title: str, credits: str, className: str = None, style: dict = None) -> None:
    self.title = title
    self.credits = credits
    self.className = className
    self.style = style
    
  
  def create(self):
    return \
      html.Div(
        style=self.style,
        className=self.className,
        children=[
          html.Div(
            className='text-center',
            children=[
            html.H4(self.title),
            html.P(self.credits, style={'fontStyle': 'italic'}, className="pb-4")
          ]),
          
          # html.Div([
          #   dcc.Dropdown([
          #       {
          #         "label": dcc.Link(children='Overview', href='/literature'),
          #         'value': 'Overview'
          #       },
          #       {
          #         "label": dcc.Link(children='Features', href='/literature/features'),
          #         'value': 'Features'
          #       },
          #       {
          #         "label": dcc.Link(children='Models', href='/literature/models'),
          #         'value': 'Models'
          #       },
          #       {
          #         "label": dcc.Link(children='Other', href='/literature/other'),
          #         'value': 'Other Visualizations'
          #       },
          #     ],
          #     value='Literature Analysis',
          #     className='container btn btn-secondary bg-grey'
          #   )
          # ],
          #   className='literature',
          # ),
          html.Div(
            className='px-3',
            children=[
              html.H4('Contents'),
              html.Div(
                className='row',
                children=[
                  html.Div(
                    className='col-6 col-lg-12',
                    children=[
                      html.P('Literature Analysis', className='bg-light text-black display-block overflow-auto mt-2 px-2'),
                      html.Div(
                        className='literature-content',
                        children=[
                          html.A(children='Overview', href='/literature'),
                          html.A(children='Features', href='/literature/features'),
                          html.A(children='Models', href='/literature/models'),
                          html.A(children='Other', href='/literature/other'),
                        ]
                      )
                    ]  
                  ),
                  html.Div(
                    className='col-6 col-lg-12',
                    children=[
                      html.P('Dataset (in progress)', className='bg-light text-black display-block overflow-auto mt-2 px-2'),
                      html.Div(
                        className='dataset-content',
                        children=[
                          html.A(children='Price', href='/literature'),
                          html.A(children='Listings', href='/literature/features'),
                          html.A(children='Hosts', href='/literature/models'),
                          html.A(children='Amenities', href='/literature/other')
                        ]
                      )
                    ]
                  )
                ]
              )
            ]
          )
        ]
      ) 