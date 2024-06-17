from domain_models.image import Image
from services import image_service
from sqlalchemy import Engine

def test_images(db_engine: Engine):

    # Arrange
    urls = ["img1", "img2"]

    #Act
    for url in urls:
        image_service.add_image(image_url=url)

    images = image_service.list_images()

    #Assert
    assert len(images) == 2
    actual_image_urls =[image.image_url for image in images]  #list comprehension
    assert set(urls) == set(actual_image_urls)
    

    # actual_image_urls = []

    # for image in inages:
    #     actual_image_urls.append(image.image_url)