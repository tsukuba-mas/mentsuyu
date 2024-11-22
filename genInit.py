import json
import numpy as np
import networkx as nx

def dumpAsJson[T](path: str, content: dict[str, T]):
    """
    Save `content` as a JSON format to the file `path`.
    """
    with open(path, "w") as f:
        json.dump(content, f)

def generateInitialBeliefs(agents: int, atoms: int, seed: int, path: str):
    """Generate initial beliefs using `atoms` atomic propositions and save to `path` as JSON format."""
    rng = np.random.default_rng(seed)
    interpretations = pow(2, atoms) - 1
    beliefs = [f"{bel:b}".zfill(interpretations) for bel in rng.integers(low=1, high=interpretations, size=agents)]
    jsonDict = {str(i): beliefs[i] for i in range(agents)}
    dumpAsJson(path, jsonDict)

def generateInitialOpinions(agents: int, topics: list[str], seed: int, path: str, ub: int = 1000000):
    """Generate initial opinions toward `topics` and save to `path` as JSON format."""
    rng = np.random.default_rng(seed)
    jsonDict = {}
    for i in range(agents):
        jsonDict[str(i)] = {}
        for topic in topics:
            jsonDict[str(i)][topic] = f"{rng.integers(low=0, high=ub)}/{ub}"
    dumpAsJson(path, jsonDict)

def generateRandomGraph(agents: int, edges: int, seed: int, path: str):
    """
    Generate initial network with `agents` nodes and `edges` edges and save to `path` as JSON format.
    If generated graph does not satisfy that all of the out degrees are positive (e.g., non-zero),
    `AssertionError` will be raised.
    """
    G = nx.gnm_random_graph(agents, edges, seed, directed=True)
    jsonDict = {str(i): list(G.neighbors(i)) for i in range(agents)}
    assert all(range(agents), lambda x: 0 < len(jsonDict[str(x)]))
    dumpAsJson(path, jsonDict)

