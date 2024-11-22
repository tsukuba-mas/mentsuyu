import pandas as pd
from .. import reader

def test_readop():
    df = reader.readop("tests/files/ophist.csv")
    expected = pd.DataFrame({
        0: [0.0, 0.5, 1.0],
        1: [1.0, 0.5, 0.0],
    }, index=[0, 1, 2]).transpose()
    assert (df == expected).all().all()

def test_readbel():
    df = reader.readbel("tests/files/belhist.csv")
    expected = pd.DataFrame({
        0: ["0001", "0010", "0011"],
        1: ["1001", "1010", "1011"],
    }, index=[0, 1, 2]).transpose()
    assert (df == expected).all().all()