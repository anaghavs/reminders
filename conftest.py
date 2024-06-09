import pytest
from sqlalchemy import create_engine
from persistence.db_setup import create_tables


def pytest_configure(config):
    import sys
    sys._called_from_test = True


def pytest_unconfigure(config):
    import sys
    del sys._called_from_test

@pytest.fixture
def db_engine():
    engine = create_engine("sqlite:///:memory:")
    create_tables(engine=engine)
    return engine
