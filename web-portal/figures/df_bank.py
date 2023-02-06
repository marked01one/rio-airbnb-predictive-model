import pandas as pd


class DataFrameBank:
  """
  Class-based data structure that holds Pandas DataFrames
  
  ---
  ## Keyword arguments:
  
  * Keyword: `df_name` -- give your figure(s) a preferred name
  * Arguments: `csv_directory` -- the CSV directory of your figures 
  
  ### Example:
  ```python
  new_figure_bank = FigureBank(
    df1="./figures/fig1.csv",
    df2="./figures/fig2.csv",
    df3="./figures/fig3.csv",
  )
  ```
  
  * Return: an dictionary-like object which contain all DataFrames you have entered into the structure
  """
  def __init__(self, **kwargs: str | pd.DataFrame) -> None:
    self.kwargs_main = None
    self.add_or_edit_df(kwargs)
    
    
  def add_or_edit_df(self, **kwargs: str | pd.DataFrame) -> None:
    """Add or edit new DataFrames into the structure
    
    ---
    ## Inputs
    * ArgumentName: the name of your DataFrame(s)
    * Argument: your DataFrame object(s) or CSV directories
    """
    for key, val in kwargs.items():
      
      if type(val) == str:
        self.kwargs_main[key] = pd.read_csv(val)
      else:
        self.kwargs_main[key] = val
  
  
  def delete_df(self, *args: str) -> None:
    """Delete chosen DataFrames
    
    ---
    ## Inputs:
    * Arguments: names of DataFrames you want to remove
    """
    for df in args:
      if df in self.kwargs_main.keys():
        del self.kwargs_main[df] 
  
  
  def list_df(self) -> list:
    """Return list of all DataFrames

    ## Returns:
    * `list` -- list of names of all DataFrames
    """
    return list(self.kwargs_main.keys())    
  
  
  def get_specific_df(self, df_name: str) -> pd.DataFrame:
    return self.kwargs_main[df_name]
  


