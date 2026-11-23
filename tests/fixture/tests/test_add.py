from kubex_py_fixture import add


def test_add() -> None:
    assert add(1, 2) == 3
