import pandas as pd
import networkx as nx
import linecache

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
    us = linecache.getline(path, 0).split(",")
    vs = linecache.getline(path, tick + 1).split(",")
    return [(int(u), int(v)) for (u, v) in zip(us, vs)]

def readgr_nx(path: str, tick: int) -> nx.DiGraph:
    edges = readgr_list(path, tick)
    return nx.DiGraph(edges)