from typing import List
import dash
from dash import html, dcc 


class Footer:
  def __init__(self, statement: str, github_link: str, hyperlink_text: str, className: str = None) -> None:
    self.statement = statement
    self.github_link = github_link
    self.hyperlink_text = hyperlink_text
    self.className = className
    
  def create(self):
    return \
      html.Div(
        className=self.className,
        children=[
          html.P(self.statement, style={
            "textAlign": "center",
            "fontStyle": "italic"
          }),
          html.A(
            href=self.github_link,
            children=self.hyperlink_text
          )
        ]
      )