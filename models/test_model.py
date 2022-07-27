from sqlalchemy import Column, Integer, String
from models.config import Base


class ModelA(Base):
    __tablename__ = 'model_a'
    Base.test = ""
    id = Column(Integer, primary_key=True)
    a = Column(String)
    b = Column(String, nullable=False)
    c = Column(String, nullable=False, default="asdasd")