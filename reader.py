import pandas as pd
import networkx as nx
import linecache
import os

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

def readgr_list(path: str, tick: int) -> list[tuple[int, int]]:
    # line number is 1-indexed
    if not os.path.exists(path):
        raise OSError(f"File {path} does not exist.")
    us = linecache.getline(path, 1).split(",")[1:] # remove tick
    vs = linecache.getline(path, tick + 2).split(",")[1:]
    return [(int(u), int(v)) for (u, v) in zip(us, vs)]

def readgr_nx(path: str, tick: int) -> nx.DiGraph:
    edges = readgr_list(path, tick)
    return nx.DiGraph(edges)