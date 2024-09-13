from pydantic import BaseModel

class ProductCreate(BaseModel):
    title: str

class ProductUpdate(BaseModel):
    title: str

class ProductResponse(BaseModel):
    id: int
    title: str
    img_url: str

    class Config:
        orm_mode = True
