import pandas as pd

def readop(path: str) -> pd.DataFrame:
    return pd.read_csv(path, index_col=0, header=None)

def readbel(path: str) -> pd.DataFrame:
    return pd.read_csv(path, index_col=0, header=None, dtype=str)