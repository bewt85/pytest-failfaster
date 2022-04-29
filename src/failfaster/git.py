from multiprocessing.sharedctypes import Value
import subprocess

from typing import List

def commits() -> List[str]:
    """
    Returns a list of commits, most recent first
    """

    try:
        p = subprocess.run(['git', 'log', '--format="%H"'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # We might not be in a git repo
        # or git might not be installed
        return []
    commits = [c for c in (c.strip('"').strip("'") for c in p.stdout.split('\n')) if c]
    return commits