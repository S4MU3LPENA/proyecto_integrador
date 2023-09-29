from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DECIMAL
from config.db import meta, engine

products = Table(
    "products",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
    ),
    Column("price", DECIMAL(precision=10,scale=2)),
    Column("Stock", Integer),
    Column("Category", Integer),
)

Categories = Table(
    "categorys",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
    ),
)


meta.create_all(engine)