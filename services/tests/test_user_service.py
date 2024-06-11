from datetime import datetime
from sqlalchemy import Engine
from services import user_service
from domain_models.user import User

def test_user(db_engine: Engine):
    # Arrange
    name = "Anagha Shenoy"
    email = "anagha.1512@gmail.com"
    password = "Th1$1SN0tMyR3@lP@$$w0rd"

    # Act and assert
    user_service.register_user(name=name, email=email, password=password)
    assert user_service.verify_user_password(email=email, password=password) is True
    assert user_service.verify_user_password(email=email, password="S0m30th3rP@$$w0rd") is False
