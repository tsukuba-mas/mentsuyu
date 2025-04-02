import pandas as pd
import networkx as nx
import linecache
import os

def makeDfColumn0origin(raw: pd.DataFrame) -> pd.DataFrame:
    df = raw.copy(deep=True)
    df.columns = list(range(df.shape[1]))
    return df

def readop(
    path: str = "",  # For backward compatibility ...
    *,
    resdir: str = "results",
    exp: str = "",
    opid: int = 0,
) -> pd.DataFrame:
    filepath = f"{resdir}/{exp}/ophist{opid}.csv" if len(exp) > 0 else path
    df = pd.read_csv(filepath, index_col=0, header=None)
    return makeDfColumn0origin(df)

def readbel(
    path: str = "",
    *,
    resdir: str = "results",
    exp: str = "",
) -> pd.DataFrame:
    filepath = f"{resdir}/{exp}/belhist.csv" if len(exp) > 0 else path
    df = pd.read_csv(filepath, index_col=0, header=None, dtype=str)
    df.index = df.index.astype(int)
    return makeDfColumn0origin(df)

def readgr_list(
    path: str = "", 
    tick: int = 0,
    *,
    resdir: str = "results",
    exp: str = "",
) -> list[tuple[int, int]]:
    filepath = f"{resdir}/{exp}/grhist.csv" if len(exp) > 0 else path

    # line number is 1-indexed
    if not os.path.exists(filepath):
        raise OSError(f"File {filepath} does not exist.")
    us = linecache.getline(filepath, 1).split(",")[1:] # remove tick
    vs = linecache.getline(filepath, tick + 2).split(",")[1:]
    return [(int(u), int(v)) for (u, v) in zip(us, vs)]

def readgr_nx(
    path: str = "", 
    tick: int = 0,
    *,
    resdir: str = "results",
    exp: str = "",
) -> nx.DiGraph:
    edges = readgr_list(path=path, resdir=resdir, exp=exp, tick=tick)
    nodes = max([u for (u, _) in edges])
    G = nx.DiGraph()
    G.add_nodes_from(range(nodes))
    G.add_edges_from(edges)
    return G