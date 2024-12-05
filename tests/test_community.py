from .. import community

def test_getBeliefBasedCommunity():
    bels = [
        "00",
        "00",
        "01",
        "10",
        "01",
        "11",
        "10",
        "00",
        "10",
        "00",
    ]
    actual = community.getBeliefBasedCommunity(bels)
    assert actual == [
        {0, 1, 7, 9},
        {3, 6, 8},
        {2, 4},
        {5},
    ]

def test_getOpinionBasedCommunity():
    opinions = [
        [0.0, 0.0],
        [0.01, 0.0],
        [0.5, 0.7],
        [1.0, 1.0],
        [0.01, 0.01],
        [0.97, 0.965]
    ]
    actual = community.getOpinionBasedCommunity(opinions)
    assert actual == [
        {0, 1, 4},
        {3, 5},
        {2},
    ]

    opinions = [
        [0.715], [0.571], [0.643], [0.357], [0.214], [0.143], [0.5],
        [0.0], [0.28]
    ]
    assert len(community.getOpinionBasedCommunity(opinions)) == 6

def test_averageEdgesBetweenCommunities():
    communities = [
        {0, 1, 2},
        {3, 4},
        {5},
    ]
    edges = [
        (0, 1), (1, 2), (2, 0),
        (3, 4),
        (1, 3), {3, 5}
    ]
    actual = community.averageEdgesBetweenCommunities(communities, edges)
    assert abs(actual - 2 / 6) <= 1e-5