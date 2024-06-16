from sqlalchemy import text

CREATE_USER_TABLE = """
    CREATE TABLE users (
        id integer NOT NULL PRIMARY KEY,
        name varchar(255),
        email varchar(255),
        password_hash varchar(1024)
    );
"""

CREATE_UNIQUE_INDEX_ON_USER_EMAIL = """
CREATE UNIQUE INDEX uidx_user_email on users (email);
"""


CREATE_REMINDER_TABLE = """
    CREATE TABLE reminders (
        id integer NOT NULL PRIMARY KEY,
        title varchar(255),
        due_date DATETIME NOT NULL,
        user_id integer NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
"""

def drop_tables(engine):
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS reminders;"))
        connection.execute(text("DROP TABLE IF EXISTS users;"))


def create_tables(engine):
    with engine.connect() as connection:
        connection.execute(text(CREATE_USER_TABLE))
        connection.execute(text(CREATE_UNIQUE_INDEX_ON_USER_EMAIL))
        connection.execute(text(CREATE_REMINDER_TABLE))
        connection.commit()

