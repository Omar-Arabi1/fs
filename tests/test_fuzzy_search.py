from fs_omar_arabi.fuzzy_search.fuzzy_search import fuzzy_search

def test_fuzzy_search():
    got = fuzzy_search(dir='.', pattern="pypr")
    want = ["pyproject.toml"]
    assert got == want
