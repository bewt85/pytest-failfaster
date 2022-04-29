from setuptools import setup

setup(
    name="pytest-failfaster",
    packages=["failfaster"],
    package_dir={'': 'src'},
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["failfaster = failfaster.plugin"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
    requires=['pytest', 'requests']
)
