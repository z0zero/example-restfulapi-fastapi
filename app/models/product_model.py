from sqlalchemy import Column, Integer, String
from app.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    img_url = Column(String(255), nullable=False)
