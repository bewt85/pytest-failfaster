import pytest

from .git import commits

def test_ids(session):
    return [i.nodeid for i in session.items]

@pytest.hookimpl(hookwrapper=True)
def pytest_collection_finish(session):
    yield
    session.items.sort(key=lambda v: ('5' in v.nodeid, v.nodeid))
    print(f"Tests Collected:\n  " + "\n  ".join(test_ids(session)))
    print(f"Commits Collected:\n  " + "\n  ".join(commits()))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    result = yield
    if result.excinfo:
        print("HERE", item.nodeid, result.excinfo)