from fastapi import APIRouter, status
from config.db import conn
from models.products import products, Categories
from schemas.products import product, categories
from typing import List
from sqlalchemy import create_engine, Table, MetaData, select

product = APIRouter()
URL = '/products'

@product.get( URL)
async def get_products():
    result = conn.execution_options(stream_results=True).execute(text("select * from products"))
    return result
""" user_table.join(address_table,
user_table.c.id == address_table.c.user_id)
stmt = select(user_table).select_from(j) """