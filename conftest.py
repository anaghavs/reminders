import pytest
from sqlalchemy import create_engine
from persistence.db_setup import create_tables


@pytest.fixture
def db_engine():
    engine = create_engine("sqlite:///:memory:")
    create_tables(engine=engine)
    return engine
