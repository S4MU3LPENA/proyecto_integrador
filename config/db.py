from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:ddr210615@localhost:3306/PROYECTO_INTEGRADOR")

meta = MetaData()

conn = engine.connect()