from datetime import datetime
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from domain_models.user import User

class UserRepo:

    def __init__(self, session: Session) -> None:
        self._session = session


    def add_user(self, user: User) -> None:
        self._session.execute(
            text(
                """
                INSERT INTO  users (name, email, password_hash) VALUES (
                    :name,
                    :email,
                    :password_hash
                )
                """
            ),
            [{"name": user.name, "email": user.email, "password_hash": user.password_hash}]
        )
   

    def get_user_by_email(self, email: str) -> User:
        db_results = self._session.execute(
            text(
                """
                SELECT name, email, password_hash
                FROM users
                WHERE email = :email
                LIMIT 1
                """
            ), [
                {"email": email}
            ]
        )

        user = None

        for row in db_results:
           user = User(name=row.name, email=row.email, password_hash=row.password_hash)

        return user