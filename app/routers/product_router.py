from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse
from app.controllers.product_controller import (
    create_product_controller,
    get_product_controller,
    get_all_products_controller,
    update_product_controller,
    delete_product_controller
)
from app.database import SessionLocal, engine, Base

# Pastikan semua tabel terbuat
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductResponse)
async def upload_product(
    title: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if image.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Tipe gambar tidak valid")

    product = create_product_controller(db, title, image)
    return product

@router.get("/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_controller(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    return product

@router.get("/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_all_products_controller(db)
    return products

@router.put("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    product = update_product_controller(db, product_id, product_update)
    if not product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    return product

@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    product = delete_product_controller(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    return product