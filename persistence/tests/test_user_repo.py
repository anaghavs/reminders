from datetime import datetime
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from domain_models.user import User
from persistence.user_repo import UserRepo


def test_user_repo(db_engine: Engine) -> None:
    user = User(name="Anagha Shenoy", email="anagha.1512@gmail.com", password_hash="1234")

    with Session(db_engine) as session:
        user_repo = UserRepo(session=session)
        user_repo.add_user(user)
        session.commit()

    
    with Session(db_engine) as session:
        user_repo = UserRepo(session=session)
        actual_user = user_repo.get_user_by_email("anagha.1512@gmail.com")
        assert user == actual_user


