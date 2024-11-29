import networkx as nx

def mix(low: tuple[int, int, int], high: tuple[int, int, int], rat: float) -> str:
    mixed = (
        int(low[0] * (1 - rat) + high[0] * rat),
        int(low[1] * (1 - rat) + high[1] * rat),
        int(low[2] * (1 - rat) + high[2] * rat),
    )
    return f"{mixed[0]:02x}{mixed[1]:02x}{mixed[2]:02x}"

def drawWithOpinions(
    G: nx.DiGraph, opinions: list[float],
    lowest = (0, 0, 255), highest = (255, 0, 0)
):
    colors = [mix(lowest, highest, o) for o in opinions]
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, node_color=colors)