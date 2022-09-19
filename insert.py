import datetime
from base import Session, engine, Base
from jupyter_db import JupyterDb
Base.metadata.create_all(engine)
session = Session()


def insert_to_db(name, file_path, created_date, updated_date):
    new_notebook = JupyterDb(
        name=name,
        file_path=file_path,
        created_date=created_date,
        updated_date=updated_date,
    )

    session.add(new_notebook)
    session.commit()
    print(f'Object - {name} inserted')

    session.close()


def read_from_db(file_name):
    return session.query(JupyterDb).filter(JupyterDb.name == file_name).first()


def read_from_db_by_id(id):
    return session.query(JupyterDb).filter(JupyterDb.id == id).first()


def delete_from_db(file_id):
    try:
        session.query(JupyterDb).filter(JupyterDb.id == file_id).delete()
        session.commit()
    except Exception as e:
        return e
    return True

def update_file_in_db(file_from_db, update_time, file_name):
    file_from_db.file_path = '/notebooks/' + file_name
    file_from_db.updated_time = update_time
    session.commit()
    return True

