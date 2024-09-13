from fastapi import FastAPI
from app.routers import product_router
from app.middleware.error_handler import GlobalExceptionHandlerMiddleware

app = FastAPI()

app.add_middleware(GlobalExceptionHandlerMiddleware)

app.include_router(product_router.router)
