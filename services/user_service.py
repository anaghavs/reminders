import bcrypt
from domain_models.user import User
from persistence.user_repo import UserRepo
from persistence.unit_of_work import UnitOfWork

# from https://dev.to/shittu_olumide_/python-hashing-and-salting-4dea
def get_password_hash(password: str):
    encoded_password = password.encode()
    salt = b'$2b$12$JiDMa1LBMKjVUR9F2JvgMO'
    hashed_password = bcrypt.hashpw(password=encoded_password, salt=salt)
    return hashed_password


def verify_password_hash(password_to_verify, hashed_password):
    encoded_password = password_to_verify.encode()
    return bcrypt.checkpw(encoded_password, hashed_password)


def register_user(name: str, email: str, password: str):
    with UnitOfWork() as uow:
        with uow.get_session() as session:
            user = User(name=name, email=email, password_hash=get_password_hash(password))
            user_repo = UserRepo(session=session)
            user_repo.add_user(user)
            session.commit()



def verify_user_password(email: str, password: str) -> bool:
    with UnitOfWork() as uow:
        with uow.get_session() as session:
            user_repo = UserRepo(session=session)
            user = user_repo.get_user_by_email(email)
            return verify_password_hash(password_to_verify=password, hashed_password=user.password_hash)

