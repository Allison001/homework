from backend import db


def test_creat_db():
    db.create_all()