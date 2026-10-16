from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/mot_db"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
