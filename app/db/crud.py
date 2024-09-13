from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.schemas.product_schema import ProductUpdate

def create_product(db: Session, title: str, img_url: str):
    new_product = Product(title=title, img_url=img_url)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_all_products(db: Session):
    return db.query(Product).all()

def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        product.title = product_update.title
        db.commit()
        db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product