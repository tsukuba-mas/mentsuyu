from .. import genInit

AGENTS = 5
IDS = {str(i) for i in range(AGENTS)}

def test_generateInitialBeliefs():
    beliefs = genInit.generateInitialBeliefs(3000, 3, 42)
    assert set(beliefs.keys()) == {str(i) for i in range(3000)}
    hasOccured = [False] * 256
    hasOccured[0] = True
    for bel in beliefs.values():
        enc = int(bel, 2)
        assert 1 <= enc <= 255
        hasOccured[enc] = True
    assert all(hasOccured)

def test_generateInitialOpinions():
    TOPICS = ["0", "1"]
    actual = genInit.generateInitialOpinions(AGENTS, TOPICS, 42)
    assert set(actual.keys()) == IDS
    assert all([len(actual[id]) == len(TOPICS) for id in IDS])
    for id in IDS:
        for i, topic in enumerate(TOPICS):
            den, num = actual[id][i].split("/")
            assert 0 <= int(den) <= int(num)

def test_generateRandomGraph():
    EDGES = 20
    actual = genInit.generateRandomGraph(AGENTS, EDGES, 42)
    assert set(actual.keys()) == IDS
    assert all([0 < len(actual[id]) for id in IDS])
    assert sum([len(actual[id]) for id in IDS]) == EDGES