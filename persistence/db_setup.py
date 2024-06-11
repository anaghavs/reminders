from sqlalchemy import text

CREATE_REMINDER_TABLE = """
    CREATE TABLE reminders (
        id integer NOT NULL PRIMARY KEY,
        title varchar(255),
        due_date DATETIME NOT NULL
    );
"""

CREATE_USER_TABLE = """
    CREATE TABLE users (
        id integer NOT NULL PRIMARY KEY,
        name varchar(255),
        email varchar(255),
        password_hash varchar(1024)
    );
"""


def create_tables(engine):
    with engine.connect() as connection:
        connection.execute(text(CREATE_REMINDER_TABLE))
        connection.execute(text(CREATE_USER_TABLE))
        
        connection.commit()

