import sys
from contextlib import contextmanager
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from persistence.db_setup import create_tables, drop_tables

if hasattr(sys, '_called_from_test'):
    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    drop_tables(engine=engine)
    create_tables(engine=engine)
else:
    engine = sqlalchemy.create_engine("sqlite:///reminders.db")
    

Session = sessionmaker(bind=engine)

class UnitOfWork:
    def __init__(self):
        self.session = None
    
    def __enter__(self):
        self.session = Session()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()


    @contextmanager
    def get_session(self):
        """Helper function to manage sessions"""
        session = Session()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()
