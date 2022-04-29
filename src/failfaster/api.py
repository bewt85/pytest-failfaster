import os
import requests

from typing import List, Optional

SUCCESS = "SUCCESS"
FAILURE = "FAILURE"

API_URL=os.environ.get('FAILFASTER', 'https://failfaster.fly.dev')
API_VERSION=2

def sort_tests(tests: List[str], commits: List[str]) -> Optional[str]:
    r = requests.post(
        f"{API_URL}/run",
        json=dict(
            commits=commits,
            tests=tests,
            version=API_VERSION,
        ),
        timeout=10,
    )
    try:
        data = r.json()
        data['url'] = API_URL + data['url']
        return data
    except:
        return None

def record_results(run_id: str, test: str, status: str, duration: float):
    requests.patch(
        f"{API_URL}/run/{run_id}",
        json=dict(
            results={ test: (status, duration) },
            version=API_VERSION,
        )
    )
