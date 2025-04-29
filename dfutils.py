import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from collections.abc import Callable
import os

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

def load_df(csv_path: str, callback: Callable[[], pd.DataFrame], index_col=0) -> pd.DataFrame:
    """
    Build Pandas DataFrame from `csv_path` if it exists;
    otherwise build it by executing `callback` and save it to `csv_path`.
    """
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path, index_col=index_col)
    else:
        result = callback()
        result.to_csv(csv_path)
        return result

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
