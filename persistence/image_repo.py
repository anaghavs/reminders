from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import text
from domain_models.reminder import Reminder
from domain_models.user import User
from domain_models.image import Image

class ImageRepo:

    def __init__(self, session: Session) -> None:
        self._session = session

    def add_image(self, image: Image) -> None:
        self._session.execute(
            text(
                """
                INSERT INTO images (image_url) VALUES(
                :image_url
                )
                """
            ),
            [{"image_url":image.image_url}]
        )


    def list_images(self ) -> List[Image]:
        db_results = self._session.execute(
            text(
                """
                SELECT image_url FROM images"""
            )
        )

        results = []

        for row in db_results:
            image = Image(image_url=row.image_url)
            results.append(image)

        return results

