# main.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User
import os

# MySQLの設定に合わせて変更してください。
token = os.environ["MYSQL_ROOT_PASSWORD"]
token = os.environ["MYSQL_ROOT_PASSWORD"]
token = os.environ["MYSQL_ROOT_PASSWORD"]
token = os.environ["MYSQL_ROOT_PASSWORD"]

DATABASE_URL = "mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>"

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_user(name, age):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    session.close()
