from .. import genInit

AGENTS = 5
IDS = {str(i) for i in range(AGENTS)}

def test_generateInitialBeliefs():
    beliefs = genInit.generateInitialBeliefs(AGENTS, 2, 42)
    assert set(beliefs.keys()) == IDS
    for id in IDS:
        assert beliefs[id] in {"01", "10", "11"}

def test_generateInitialOpinions():
    TOPICS = ["0", "1"]
    actual = genInit.generateInitialOpinions(AGENTS, TOPICS, 42)
    assert set(actual.keys()) == IDS
    assert all([set(actual[id]) == set(TOPICS) for id in IDS])
    for id in IDS:
        for topic in TOPICS:
            den, num = actual[id][topic].split("/")
            assert 0 <= int(den) <= int(num)

def test_generateRandomGraph():
    EDGES = 20
    actual = genInit.generateRandomGraph(AGENTS, EDGES, 42)
    assert set(actual.keys()) == IDS
    assert all([0 < len(actual[id]) for id in IDS])
    assert sum([len(actual[id]) for id in IDS]) == EDGES