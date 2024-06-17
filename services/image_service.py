import bcrypt
from domain_models.image import Image
from persistence.image_repo import ImageRepo
from persistence.unit_of_work import UnitOfWork

def add_image(image_url: str):
    with UnitOfWork() as uow:
        with uow.get_session() as session:
            image = Image(image_url=image_url)
            image_repo = ImageRepo(session=session)
            # image = image_repo.list_images()

            image_repo.add_image(image)
            session.commit()

def list_images():
    with UnitOfWork() as uow:
        with uow.get_session() as session:
            image_repo = ImageRepo(session=session)
            return image_repo.list_images()


    
