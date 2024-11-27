import json
import numpy as np
import networkx as nx

def dumpAsJson[T](path: str, content: dict[str, T]):
    """
    Save `content` as a JSON format to the file `path`.
    """
    with open(path, "w") as f:
        json.dump(content, f)

def generateInitialBeliefs(agents: int, atoms: int, seed: int) -> dict[str, str]:
    """Generate initial beliefs using `atoms` atomic propositions"""
    rng = np.random.default_rng(seed)
    interpretations = pow(2, atoms)
    possibleModels = pow(2, interpretations)
    beliefs = [f"{bel:b}".zfill(interpretations) for bel in rng.integers(low=1, high=possibleModels, size=agents)]
    return {str(i): beliefs[i] for i in range(agents)}
    

def generateInitialBeliefsJson(agents: int, atoms: int, seed: int, path: str):
    json = generateInitialBeliefs(agents, atoms, seed)
    dumpAsJson(path, json)

def generateInitialOpinions(agents: int, topics: list[str], seed: int, ub: int = 1000000) -> dict[str, dict[str, float]]:
    """Generate initial opinions toward `topics`"""
    rng = np.random.default_rng(seed)
    jsonDict = {}
    for i in range(agents):
        jsonDict[str(i)] = {}
        for topic in topics:
            jsonDict[str(i)][topic] = f"{rng.integers(low=0, high=ub)}/{ub}"
    return jsonDict
    

def generateInitialOpinionsJson(agents: int, topics: list[str], seed: int, path: str, ub: int = 1000000):
    """Generate initial opinions toward `topics` and save to `path` as JSON format."""
    json = generateInitialOpinions(agents, topics, seed, ub)
    dumpAsJson(path, json)

def generateRandomGraph(agents: int, edges: int, seed: int):
    """
    Generate initial network with `agents` nodes and `edges` edges.
    """
    # To assume that 1 <= out-degree for all nodes ...
    rng = np.random.default_rng(seed)
    d = {a: [] for a in range(agents)}
    for a in range(agents):
        while True:
            b = rng.integers(0, agents)  # output an integer in [0, agents)
            if b == a:
                continue
            d[a].append(b)
            break

    current = agents
    while current < edges:
        a = rng.integers(0, agents)
        b = rng.integers(0, agents)
        if a == b or b in d[a]:
            continue
        d[a].append(b)
        current += 1
    
    return {str(a): d[a] for a in d}

def generateRandomGraphJson(agents: int, edges: int, seed: int, path: str):
    """
    Generate initial network with `agents` nodes and `edges` edges and save to `path` as JSON format.
    If generated graph does not satisfy that all of the out degrees are positive (e.g., non-zero),
    `AssertionError` will be raised.
    """
    json = generateRandomGraph(agents, edges, seed)
    dumpAsJson(path, json)


if __name__ == "__main__":
    import argparse
    import os
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", type=int, help="# of agents", default=100)
    parser.add_argument("--seed", type=int, help="seed", default=42)
    parser.add_argument("--edge", type=int, help="# of edges", default=400)
    parser.add_argument("--atom", type=int, help="# of atoms", default=3)
    parser.add_argument("--topic", type=str, help="topics", default="11110000")
    parser.add_argument("--dir", type=str, help="output dir", default="")
    parser.add_argument("--opinion", action="store_true")
    parser.add_argument("--belief", action="store_true")
    parser.add_argument("--graph", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(args.dir):
        os.mkdir(args.dir)

    if args.opinion:
        generateInitialOpinionsJson(
            args.agent, args.topic.split(","), args.seed,
            os.path.join(args.dir, f"opinions-{args.seed}.json")
        )
    if args.belief:
        generateInitialBeliefsJson(
            args.agent, args.atom, args.seed,
            os.path.join(args.dir, f"beliefs-{args.seed}.json")
        )
    if args.graph:
        generateRandomGraphJson(
            args.agent, args.edge, args.seed,
            os.path.join(args.dir, f"graph-{args.seed}.json")
        )