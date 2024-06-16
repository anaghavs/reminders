from domain_models.image import Image
from persistence.image_repo import ImageRepo
from sqlalchemy.orm import Session
from sqlalchemy import Engine

def test_image_repo(db_engine:Engine) -> None:
    image_url1 = "url1"
    image_url2 = "url2"

    image1 = Image(image_url=image_url1)
    image2 = Image(image_url=image_url2)

    with Session(db_engine) as session:

        image_repo= ImageRepo(session=session)
        image_repo.add_image(image=image1)
        image_repo.add_image(image=image2)
        session.commit()

    with Session(db_engine) as session:
        image_repo = ImageRepo(session=session)
        images = image_repo.list_images()

        assert image1 in images
        assert image2 in images
        assert len(images) == 2