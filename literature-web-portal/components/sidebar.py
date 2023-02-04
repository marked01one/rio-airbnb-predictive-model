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
          html.H4(self.title),
          html.P(self.credits, style={'fontStyle': 'italic'}, className="pb-4"),
          html.Div([
            html.Div([
              dcc.Link(
                f"{page['name']}", 
                href=page['relative_path'],
                className=f"btn btn-success d-flex my-4"
              )
              for page in dash.page_registry.values()
            ],
            className='container')
          ])
        ]
      )
  