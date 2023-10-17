
SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:jenr2023@localhost:5432/blogposts_db"


class Config:
    DEBUG = False #True
    SECRET_KEY = 'jce'

    SQLALCHEMY_DATABASE_URI = POSTGRESQL

    CKEDITOR_PKG_TYPE = 'full'