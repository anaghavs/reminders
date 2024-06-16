import pytest
from persistence.unit_of_work import engine
from persistence.db_setup import create_tables, drop_tables


def pytest_configure(config):
    import sys
    sys._called_from_test = True


def pytest_unconfigure(config):
    import sys
    del sys._called_from_test

@pytest.fixture
def db_engine():
    drop_tables(engine=engine)
    create_tables(engine=engine)
    return engine
