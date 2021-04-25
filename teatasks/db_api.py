from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///data/test.db", echo=True)
Base = declarative_base()


class Lists(Base):  # type: ignore
    __tablename__ = "lists"
    list_id = Column(Integer, primary_key=True)
    list_name = Column(String)


class Items(Base):  # type: ignore
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey("lists.list_id"))
    title = Column(String)
    content = Column(String)


Base.metadata.create_all(engine)
