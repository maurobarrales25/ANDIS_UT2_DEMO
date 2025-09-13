from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    
    