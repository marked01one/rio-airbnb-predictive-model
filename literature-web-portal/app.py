from dash import Dash, html, dcc
import dash
import plotly.express as px
import pandas as pd
from components import footer, sidebar

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
    sidebar.Sidebar(
      className="col-md-2 bg-black text-white py-4 px-2 text-center",
      title='Airbnb Predictive Model',
      credits='by Minh Khoi Tran'
    ).create(),
    
    # Main content container
    html.Div(
      className="col-md-10 text-center",
      children=[
        dash.page_container,
        footer.Footer(
          statement="""
            This web portal is created to support the predictive modeling project initiated by Dr. Sonya Zhang from the 
            Computer Information Systems department of California Polytechnic State University, Pomona
          """,
          hyperlink_text='For more info on the project, click on this link',
          github_link='https://github.com/marked01one/rio-airbnb-predictive-model#-web-portals-',
          className="container mb-4"
        ).create()
      ]
    )
  ]
)



if __name__ == '__main__':
  app.run_server(debug=True)