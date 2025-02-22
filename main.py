from fastapi import FastAPI
from routes.user import user
from routes.products import product

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
)

app.include_router(user)
app.include_router(product)