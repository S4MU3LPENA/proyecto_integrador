from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DECIMAL
from config.db import meta, engine
from sqlalchemy import Table, ForeignKey, Column, Integer, Date, String

#TABLA CUSTOMER

customer = Table(
    "customer",
    meta,
    Column("customer_id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
    ),
    Column("email", String(255)),
    Column("address", String(255)),
)

#TABLA ORDER

order = Table(
    "order",
    meta,
    Column("order_id", Integer, primary_key=True),
    Column(
        "order_date",
        Date,  #si quieres ponle tipo date
    ),
    Column("delivery_id", Integer,ForeignKey("delivery.id")),
    Column("customer_id", Integer,ForeignKey("delivery.id")),
)

#TABLA PRODUCTS

products = Table(
    "products",
    meta,
    Column("product_id", Integer, primary_key=True),
    Column(
        "product_name",
        String(300),
    ),
    Column("category_id", Integer,ForeignKey("category.id")),
)

#TABLA CATEGORIES

categories = Table(
    "categories",
    meta,
    Column("category_id", Integer, primary_key=True),
    Column(
        "category_name",
        String(255),
    ),
    Column("category_type", String(255)),
    Column("field", String(255), unique=True),
)

#TABLA DELIVERY

delivery = Table(
    "delivery",
    meta,
    Column("delivery_id", Integer, primary_key=True),
    Column(
        "type",
        String(255),
    ),
    Column("status", String(255)),
)


meta.create_all(engine)
