from dash import Dash, html, dcc
import dash
import plotly.express as px
import pandas as pd 

# Import stylesheets
stylesheets = [
  {
    'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css',
    'rel': 'stylesheet',
    'integrity': "sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD",
    'crossorigin': 'anonymous'
  }
]

# Initialize app
app = Dash(
  __name__,
  external_stylesheets=stylesheets,
  use_pages=True
)

# Generate the app layout
app.layout = html.Div(
  className="row",
  style={
    'fontFamily': 'monospace'
  },
  children=[
    
    # Sidebar HTML, containing route links and project title
    html.Div(
      className="col-lg-2 bg-black text-white py-4 px-2 text-center",
      children=[
      html.H4('Airbnb Predictive Model'),
      html.P('by Minh Khoi Tran', style={'fontStyle': 'italic'}),
      html.Div([
        html.Div([
          dcc.Link(
            f"{page['name']}", 
            href=page['relative_path'],
            className=f"btn btn-success d-flex my-2"
          )
          for page in dash.page_registry.values()
        ],
        className='container')
      ])
    ]),
    html.Div(
      className="col-lg-10 text-center",
      children=dash.page_container
    )
  ]
)



if __name__ == '__main__':
  app.run_server(debug=True)