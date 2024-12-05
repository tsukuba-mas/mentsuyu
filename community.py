from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
from typing import Callable

def getBeliefBasedCommunity(bels: list[str]) -> list[set[int]]:
    """
    Returns belief-based communities by the set of agents' id (0-indexed).
    Each communities satisfy that all of the members in the community share the same belief.
    Communities are sorted with respect to the number of members in descendent order.
    """
    bel2ids = {}
    for i, bel in enumerate(bels):
        if bel in bel2ids:
            bel2ids[bel].append(i)
        else:
            bel2ids[bel] = [i]
    results = [set(c) for c in bel2ids.values()]
    results.sort(key=lambda x: len(x), reverse=True)
    return results

def getOpinionBasedCommunity(ops: list[list[float]] | list[float], eps: float = 0.1) -> list[set[int]]:
    """
    Returns opinions-based communities by the set of agents' id (0-indexed).
    Each communities satisfy that the maximal distance between opinions over the members is `eps`.
    Communities are sorted with respect to the number of members in descendent order.
    """
    twodim_ops = ops if type(ops[0]) == list else [o for o in ops]
    pdist_ops = pdist(twodim_ops, metric="euclidean")
    id2cluster = fcluster(linkage(pdist_ops, 'complete'), t=eps, criterion="distance")
    coms = {}
    for i in range(len(ops)):
        clsid = id2cluster[i]
        if clsid in coms:
            coms[clsid].append(i)
        else:
            coms[clsid] = [i]
    
    communities = [set(c) for c in coms.values()]
    communities.sort(key=lambda x: len(x), reverse=True)
    return communities

def find[T](xs: list[T], cond: Callable[[T], bool]) -> int:
    """
    Return the first index such that `cond(xs[index]) == True`.
    If there are no such elements, `-1` is returned instead.
    """
    for idx, x in enumerate(xs):
        if cond(x):
            return idx
    return -1

def averageEdgesBetweenCommunities(coms: list[set[int]], edges: list[tuple[int, int]]) -> float:
    """
    Returns the average edges between communities.
    If the number of communities is 1, float('inf') is returned.
    """
    if len(coms) == 1:
        return float('inf')
    
    cnt = 0
    for (u, v) in edges:
        idx = find(coms, lambda com: u in com)
        if v not in coms[idx]:
            cnt += 1
    return cnt / len(coms) / (len(coms) - 1)