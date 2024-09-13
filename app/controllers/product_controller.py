from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.services.product_service import (
    create_product,
    get_product,
    get_all_products,
    update_product,
    delete_product
)
from app.schemas.product_schema import ProductUpdate

def create_product_controller(db: Session, title: str, image: UploadFile):
    return create_product(db, title, image)

def get_product_controller(db: Session, product_id: int):
    return get_product(db, product_id)

def get_all_products_controller(db: Session):
    return get_all_products(db)

def update_product_controller(db: Session, product_id: int, product_update: ProductUpdate):
    return update_product(db, product_id, product_update)

def delete_product_controller(db: Session, product_id: int):
    return delete_product(db, product_id)
