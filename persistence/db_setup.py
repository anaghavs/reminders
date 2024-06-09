from sqlalchemy import text

CREATE_REMINDER_TABLE = """
    CREATE TABLE reminders (
        id integer NOT NULL PRIMARY KEY,
        title varchar(255),
        due_date DATETIME NOT NULL
    );
"""


def create_tables(engine):
    with engine.connect() as connection:
        connection.execute(text(CREATE_REMINDER_TABLE))
        
        connection.commit()

