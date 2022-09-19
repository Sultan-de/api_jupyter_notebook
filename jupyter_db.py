from sqlalchemy import Column, String, Integer, TIMESTAMP, DATETIME
from base import Base


class JupyterDb(Base):
    __tablename__ = 'jupyter_db'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    file_path = Column(String())
    created_date = Column(TIMESTAMP())
    updated_date = Column(TIMESTAMP())

    def __init__(self, name, file_path, created_date, updated_date):
        self.name = name
        self.file_path = file_path
        self.created_date = created_date
        self.updated_date = updated_date