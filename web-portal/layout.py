from dash import html
from components import footer, sidebar
import dash

# Create the app layout
def make_layout():
  return html.Div(
    className="row",
    style={
      'fontFamily': 'monospace'
    },
    children=[
      
      # Sidebar HTML, containing route links and project title
      sidebar.Sidebar(
        className="col-12 col-lg-2 bg-black text-white py-4",
        title='Airbnb Predictive Model',
        credits='by Minh Khoi Tran'
      ).create(),
      
      # Main content container
      html.Div(
        className="col-12 col-lg-10 main-body",
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