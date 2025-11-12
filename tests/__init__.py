"""
Make `tests` a package so absolute imports like `from tests.conftest import ...`
resolve to the repository's local `tests` directory instead of any site-packages
shadow packages.
"""
