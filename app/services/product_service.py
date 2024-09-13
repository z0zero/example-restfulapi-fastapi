from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.db.crud import (
    create_product as db_create_product,
    get_product as db_get_product,
    get_all_products as db_get_all_products,
    update_product as db_update_product,
    delete_product as db_delete_product
)
from app.utils.file_utils import save_upload_file
from app.schemas.product_schema import ProductUpdate

def create_product(db: Session, title: str, image: UploadFile):
    img_url = save_upload_file(image, title)
    return db_create_product(db, title, img_url)

def get_product(db: Session, product_id: int):
    return db_get_product(db, product_id)

def get_all_products(db: Session):
    return db_get_all_products(db)

def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    return db_update_product(db, product_id, product_update)

def delete_product(db: Session, product_id: int):
    return db_delete_product(db, product_id)