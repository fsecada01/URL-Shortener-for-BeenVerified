from backend import db
from urllib.parse import urlparse
from flask_validates import validates
from sqlalchemy_mixins import AllFeaturesMixin


class BaseModel(db.Model, AllFeaturesMixin):
    __abstract__ = True
    pass


class ShortenedURL(BaseModel):
    write_date = db.Column("Post Date", db.DateTime)
    original_url = db.Column("Original URL", db.string(1020))
    shortened_url = db.Column("Shortened URL", db.string(20))

    @validates("original_url")
    def validate_url(self):
        test_url = urlparse(self.original_url)
        if test_url.scheme is None or test_url.netloc is None:
            raise f"The URL {self.original_url} is not valid."
        else:
            return self.original_url
