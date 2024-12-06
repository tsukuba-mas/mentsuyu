import pandas as pd

def diff(df1: pd.DataFrame, df2: pd.DataFrame, on: list[str]) -> pd.DataFrame:
    return pd.merge(df1, df2, on=on, how ="outer", indicator=True).query(f'_merge != "both"')

# to show all of the dataframe columns
# Example:
# with showAll():
#    display(df)
class ShowAll():
    keys = [
        "display.max_columns",
        "display.max_rows",
    ]

    def __init__(self, m: int = 1000000000):
        self.m = m
        self.current = {k: None for k in self.keys}
    
    def __enter__(self):
        self.current = {k: pd.get_option(k) for k in self.keys}
        for k in self.keys:
            pd.set_option(k, self.m)
    
    def __exit__(self, exc_type, exc_value, traceback):
        for key, val in self.current.items():
            pd.set_option(key, val)
