from scipy.cluster.hierarchy import linkage, fcluster

def getBeliefBasedCommunity(bels: list[str]) -> list[set[int]]:
    """
    Returns belief-based communities by the set of agents' id (0-indexed).
    Each communities satisfy that all of the members in the community share the same belief.
    Communities are sorted with respect to the number of members in descendent order.
    """
    bel2ids = {}
    for i, bel in enumerate(bels):
        if bel in bel2ids:
            bel2ids[bel].add(i)
        else:
            bel2ids[bel] = [i]
    results = list(bel2ids.values())
    results.sort(key=lambda x: len(x), reverse=True)
    return results

def getOpinionBasedCommunity(ops: list[list[float]], eps: float = 0.1) -> list[set[int]]:
    """
    Returns opinions-based communities by the set of agents' id (0-indexed).
    Each communities satisfy that the maximal distance between opinions over the members is `eps`.
    Communities are sorted with respect to the number of members in descendent order.
    """
    id2cluster = fcluster(linkage(ops, 'ward', metric="euclidean"), t=eps, criterion="distance")
    coms = {}
    for i in range(len(ops)):
        clsid = id2cluster[i]
        if clsid in coms:
            coms[clsid].append(i)
        else:
            coms[clsid] = [i]
    
    communities = list(coms.values())
    communities.sort(key=lambda x: len(x), reverse=True)
    return communities

def averageEdgesBetweenCommunities(coms: list[set[int]], edges: list[tuple[int, int]]) -> float:
    """
    Returns the average edges between communities.
    If the number of communities is 1, float('inf') is returned.
    """
    if len(coms) == 1:
        return float('inf')
    
    cnt = 0
    for (u, v) in edges:
        idx = coms.find(lambda com, val: val in com, u)
        if v not in coms[idx]:
            cnt += 1
    return cnt / len(coms) / (len(coms) - 1)