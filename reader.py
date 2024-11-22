import pandas as pd

def makeDfColumn0origin(raw: pd.DataFrame) -> pd.DataFrame:
    df = raw.copy(deep=True)
    df.columns = list(range(df.shape[1]))
    return df

def readop(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0, header=None)
    return makeDfColumn0origin(df)

def readbel(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0, header=None, dtype=str)
    df.index = df.index.astype(int)
    return makeDfColumn0origin(df)