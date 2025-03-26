import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import hashlib

def value_to_color(val: str) -> str:
    hexcode = hashlib.sha256(val.encode()).hexdigest()
    return f"#{hexcode[:6]}"

def mix(low: tuple[int, int, int], high: tuple[int, int, int], rat: float) -> str:
    mixed = (
        int(low[0] * (1 - rat) + high[0] * rat),
        int(low[1] * (1 - rat) + high[1] * rat),
        int(low[2] * (1 - rat) + high[2] * rat),
    )
    return f"#{mixed[0]:02x}{mixed[1]:02x}{mixed[2]:02x}"

def drawWithOpinions(
    G: nx.DiGraph, opinions: list[float],
    lowest = (0, 0, 255), highest = (255, 0, 0),
    figsize=None,
    seed=42,
):
    if figsize is not None:
        _ = plt.figure(figsize=figsize)
    colors = [mix(lowest, highest, o) for o in opinions]
    pos = nx.spring_layout(G, seed=seed)
    nx.draw(G, pos=pos, node_color=colors)

def radianLists(n: int) -> list[float]:
    ## Returns the list of radians 0, 2π/n, 4π/n, ..., 2(n-1)π/n.
    return [2 * np.pi * i / n for i in range(n)]

def buildOrders(swap: list[(int, int)], l: int) -> list[int]:
    ## Returns the order of each components with respect to `swap`.
    result = list(range(l))
    for (x, y) in swap:
        result[x], result[y] = result[y], result[x]
    return result

def drawWithOpinionsWithRotating(
    G: nx.DiGraph, opinions: list[float],
    lowest = (0, 0, 255), highest = (255, 0, 0),
    figsize=None,
    radius=1.0,
    swap:list[(int, int)]=[],
):
    ## Draw network with opinions.
    ## Each opinions are represented as colors of the nodes correspond to each agents.
    if figsize is not None:
        _ = plt.figure(figsize=figsize)
    colors = [mix(lowest, highest, o) for o in opinions]
    components = list(nx.strongly_connected_components(G))
    order = buildOrders(swap, len(components))
    centers = [(radius * np.cos(rad), radius * np.sin(rad)) for rad in radianLists(len(components))]
    pos = {}
    for idx, component in enumerate(components):
        subpos = nx.spring_layout(G.subgraph(component))
        for v, p in subpos.items():
            cx, cy = centers[order[idx]]
            pos[v] = (cx + p[0], cy + p[1])
    nx.draw(G, pos=pos, node_color=colors)

def drawWithBeliefs(
    G: nx.DiGraph, beliefs: list[str],
    palette: list[str] = [],
    colormaps: dict[str, str] = {},
    seed: int = 42,
):
    bel2color = {}
    if len(palette) > 0:
        assert len(set(beliefs)) <= len(palette), f"More color needed to show {len(set(beliefs))} beliefs"
        bel2color = {b: palette[i] for i, b in enumerate(set(beliefs))}
    elif len(colormaps) > 0:
        bel2color = colormaps
    else:
        bel2color = {b: value_to_color(b) for b in set(beliefs)}
    colors = [bel2color[b] for b in beliefs]
    pos = nx.spring_layout(G, seed=seed)
    nx.draw(G, pos=pos, node_color=colors)