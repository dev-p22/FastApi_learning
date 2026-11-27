# import sqlite3
from fastapi import Depends, FastAPI

from database.database import Base, engine
from routes import todos

app = FastAPI()

app.include_router(todos.router)
# conn = sqlite3.connect("test.db", check_same_thread=False)

# cursor = conn.cursor()  # use to run sqlquery

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS  todos(
#                         id  INTEGER PRIMARY KEY,
#                         title TEXT,
#                         completed TEXT
# )
# """)
# conn.commit()


# DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )  # db connect

# sessionLocal = sessionmaker(bind=engine)  # db operations

# Base = declarative_base()


# class Todo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     completed = Column(Boolean)


Base.metadata.create_all(bind=engine)


# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



