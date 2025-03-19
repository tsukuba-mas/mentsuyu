import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

def diff(df1: pd.DataFrame, df2: pd.DataFrame, on: list[str]) -> pd.DataFrame:
    return pd.merge(df1, df2, on=on, how ="outer", indicator=True).query(f'_merge != "both"')

def plot_with_errorbar(dataframe: pd.DataFrame, groupby: str, measure: str, xlabel: str, ylabel: str, color="blue"):
     ddf = dataframe.groupby([groupby])[measure].agg(["mean", "std"])
     plt.errorbar(ddf.index, ddf["mean"], yerr=ddf["std"], color=color)
     plt.xlabel(xlabel)
     plt.ylabel(ylabel)
    
def df_to_heatmap(dataframe: pd.DataFrame, index: str, column: str, value: str, aggfunc="mean"):
    ddf = dataframe.pivot_table(index=index, columns=column, values=value, aggfunc=aggfunc)
    display(ddf.style.background_gradient(axis=None))

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
