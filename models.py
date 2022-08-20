# create a database
# books.db
# create a model
# create a view

from sqlalchemy import (create_engine, Column, Integer, String, Date)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    published = Column(Date, default=None, nullable=True, index=True)
    price = Column(Integer)
    format = Column(String)


    def __repr__(self):
        return f"<Book(title='{self.title}', " \
               f"author='{self.author}', published='{self.published}'," \
               f" price='{self.price}', format='{self.format}')> "
