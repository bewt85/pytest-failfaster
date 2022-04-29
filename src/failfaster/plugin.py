import pytest
import time

from .git import get_commits
from .api import sort_tests, record_results, SUCCESS, FAILURE

@pytest.hookimpl(hookwrapper=True)
def pytest_collection_finish(session):
    yield
    tests = { i.nodeid: i for i in session.items }
    commits = get_commits()
    resp = sort_tests(list(tests.keys()), commits)
    if resp:
        session.items = [tests[t] for t in resp['tests']]
        session.failfaster_id = resp['run_id']
        print(f"FAILFASTER: {resp['url']}")
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    started = time.time()
    result = yield
    duration = time.time() - started
    if not hasattr(item.session, 'failfaster_id'):
        return
    
    run_id = item.session.failfaster_id
    if result.excinfo:
        record_results(run_id, item.nodeid, FAILURE, duration)
    else:
        record_results(run_id, item.nodeid, SUCCESS, duration)
