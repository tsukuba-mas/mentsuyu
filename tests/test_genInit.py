from .. import genInit

AGENTS = 5
IDS = {str(i) for i in range(AGENTS)}

def test_generateInitialBeliefs():
    beliefs = genInit.generateInitialBeliefs(AGENTS, 2, 42)
    assert set(beliefs.keys()) == IDS
    is01 = is10 = is11 = False
    for id in IDS:
        if beliefs[id] == "01":
            is01 = True
        elif beliefs[id]== "10":
            is10 = True
        elif beliefs[id] == "11":
            is11 = True
        else:
            assert False
    assert is01 and is10 and is11

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