import pandas as pd

def diff(df1: pd.DataFrame, df2: pd.DataFrame, on: list[str]) -> pd.DataFrame:
    return pd.merge(df1, df2, on=on, how ="outer", indicator=True).query(f'_merge != "both"')

# to show all of the dataframe columns
# Example:
# with showAll():
#    display(df)
class ShowAll():
    key = "display.max_columns"

    def __init__(self, m: int = 1000000000):
        self.m = m
        self.current = None
    
    def __enter__(self):
        self.current = pd.get_option(self.key)
        pd.set_option(self.key, self.m)
    
    def __exit__(self):
        pd.set_option(self.key, self.current)
