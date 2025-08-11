from fs_omar_arabi.fuzzy_search.fuzzy_search import fuzzy_search

def test_fuzzy_search():
    got = fuzzy_search(dir='.', pattern="pypr", filter_by="")
    want = ["pyproject.toml"]
    assert got == want


def test_fuzzy_search_with_filter():
    got = fuzzy_search(dir='.', pattern=".gi", filter_by="files")
    want = [".gitignore"]
    assert got == want

    got = fuzzy_search(dir=".", pattern=".gi", filter_by="dirs")
    want = [".git"]
    assert got == want