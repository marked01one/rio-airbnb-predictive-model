from layout import make_layout
import dash


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
app = dash.Dash(
  __name__,
  external_stylesheets=stylesheets,
  use_pages=True
)

# Run server
if __name__ == '__main__':
  app.layout = make_layout()
  app.run_server(debug=True)